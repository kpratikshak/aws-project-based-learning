

🚀  Serverless Image Optimizer with AWS Lambda & S3 :


# 🛠️ Tech Stack:

AWS Lambda — Python 3.11 function to handle the image compression
Amazon S3 — Triggers Lambda on image uploads
IAM Roles — To grant minimal and secure permissions
Pillow — For optimizing images in Python


# Shell Scripts — To deploy and clean up resources easily


## 📁 Project Structure
serverless-image-optimizer/
├── lambda/
│   └── handler.py             # Main Lambda code
├── deploy/
│   ├── create_resources.sh    # Setup script
│   ├── delete_resources.sh    # Teardown script
│   └── trust-policy.json      # IAM trust policy
├── test-images/               # Sample images
├── requirements.txt           # Pillow dependency
└── README.md
🚀 How It Works
Upload an image (.jpg, .png) to your S3 bucket.
Lambda automatically gets triggered.
It compresses and saves the new image as optimized-filename.jpg.
Simple. Fast. Scalable. Free-tier friendly.
🧯 Avoiding AWS Charges
Cloud costs can creep up if you’re not careful. This project is:

✅ 100% AWS Free Tier compatible
✅ No long-running services (like EC2)
✅ Includes a delete_resources.sh teardown script
Run this when you’re done:

bash deploy/delete_resources.sh




