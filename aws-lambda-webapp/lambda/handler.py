import boto3
from PIL import Image
import io
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')          
QUALITY      = int(os.environ.get('IMAGE_QUALITY', '60'))
MAX_SIZE     = tuple(map(int, os.environ.get('IMAGE_MAX_SIZE', '2048,2048').split(',')))
OUTPUT_PREFIX = os.environ.get('OUTPUT_PREFIX', 'optimized-')
SUPPORTED    = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff'}


def lambda_handler(event, context):
    # ── 1. Parse & validate event ─────────────────────────────────────────────
    try:
        record = event['Records'][0]['s3']
        bucket = record['bucket']['name']
        key    = record['object']['key']
    except (KeyError, IndexError) as exc:
        logger.error("Malformed S3 event: %s", exc)
        return {'statusCode': 400, 'body': 'Invalid event structure'}

 
    filename = os.path.basename(key)
    if filename.startswith(OUTPUT_PREFIX):
        logger.info("Skipping already-optimised file: %s", key)
        return {'statusCode': 200, 'body': 'Skipped'}

    ext = os.path.splitext(key)[1].lower()
    if ext not in SUPPORTED:
        logger.warning("Unsupported file type '%s' for key: %s", ext, key)
        return {'statusCode': 415, 'body': f'Unsupported image type: {ext}'}
      
    try:
        s3_obj   = s3.get_object(Bucket=bucket, Key=key)
        metadata = s3_obj.get('Metadata', {})
        raw      = s3_obj['Body'].read()
    except s3.exceptions.NoSuchKey:
        logger.error("Object not found: s3://%s/%s", bucket, key)
        return {'statusCode': 404, 'body': 'Source object not found'}

    # ── 5. Process image 
    try:
        img = Image.open(io.BytesIO(raw))
        img.verify()                         # detect corrupt files early
        img = Image.open(io.BytesIO(raw))    # re-open after verify() exhausts the handle

        # Preserve EXIF / colour profile where possible
        exif = img.info.get('exif', b'')

        img = img.convert('RGB')

        # Down-scale only if larger than MAX_SIZE; never upscale
        img.thumbnail(MAX_SIZE, Image.LANCZOS)

        buffer = io.BytesIO()
        save_kwargs = {
            'format':   'JPEG',
            'optimize': True,
            'quality':  QUALITY,
            'progressive': True,   # progressive JPEG for faster perceived load
        }
        if exif:
            save_kwargs['exif'] = exif

        img.save(buffer, **save_kwargs)
        buffer.seek(0)
        optimized_size = buffer.getbuffer().nbytes

    except Exception as exc:
        logger.exception("Image processing failed for %s: %s", key, exc)
        return {'statusCode': 422, 'body': f'Image processing error: {exc}'}
      
    dir_part  = os.path.dirname(key)
    base_name = OUTPUT_PREFIX + os.path.splitext(filename)[0] + '.jpg'
    new_key   = os.path.join(dir_part, base_name) if dir_part else base_name

    
    try:
        s3.put_object(
            Bucket      = bucket,
            Key         = new_key,
            Body        = buffer,
            ContentType = 'image/jpeg',
            CacheControl= 'max-age=31536000',   # 1 year – immutable optimised asset
            Metadata    = {**metadata, 'source-key': key},
        )
    except Exception as exc:
        logger.exception("S3 upload failed for %s: %s", new_key, exc)
        return {'statusCode': 500, 'body': f'Upload failed: {exc}'}

    logger.info(
        "Optimised s3://%s/%s → s3://%s/%s | original=%d B optimised=%d B saved=%.1f%%",
        bucket, key, bucket, new_key,
        len(raw), optimized_size,
        (1 - optimized_size / len(raw)) * 100 if raw else 0,
    )

    return {
        'statusCode': 200,
        'body': f'Image optimised and saved as {new_key}',
        'original_size':  len(raw),
        'optimized_size': optimized_size,
    }
