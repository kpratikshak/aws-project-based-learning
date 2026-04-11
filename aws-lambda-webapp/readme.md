

🚀 Built a Serverless Image Optimizer with AWS Lambda + S3 

 Upload an image to S3 → Lambda compresses it → Optimized version appears.
Fully serverless, beginner-friendly, and no surprise AWS bills.


Whether you’re learning AWS, building portfolio projects, or automating real-world workflows — this one’s for you.

⚙️ What I Built:
Whenever you upload an image to a specific S3 bucket, it automatically triggers a Lambda function which:

1. Reads the image
2. Compresses it using Pillow (Python image library)
3. Saves an optimized version back to the bucket with the prefix optimized
This is all done in a serverless fashion — no EC2, no containers, no headache.

🛠️ Tech Stack
AWS Lambda — Python 3.11 runtime function to handle the image compression
Amazon S3 — Triggers Lambda on image uploads
IAM Roles — To grant minimal and secure permissions
Pillow — For optimizing images in Python
Shell Scripts — To deploy and clean up resources easily
