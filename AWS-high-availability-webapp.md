🚀 Fault-Tolerant Multi-AZ Web Application on AWS


This project demonstrates how to deploy a highly available, fault-tolerant web application across
multiple Availability Zones (AZs) in AWS. The architecture ensures minimal downtime, automatic failover, and scalability to handle varying traffic loads.

🏗️ Architecture:

The solution uses a multi-tier architecture with redundancy across AZs:

VPC with public and private subnets across multiple AZs
Application Load Balancer (ALB) for traffic distribution
EC2 Instances in Auto Scaling Group (ASG)
RDS (Multi-AZ) for database high availability
NAT Gateway for outbound internet access from private subnets
Security Groups & IAM Roles for secure access
⚙️ Prerequisites
AWS Account
IAM user with appropriate permissions
AWS CLI configured (aws configure)
Basic knowledge of networking and AWS services

IAC with Terraform:

🚀 Deployment Steps
1. Create VPC
Create a VPC with CIDR block (e.g., 10.0.0.0/16)
Create:
2 Public Subnets (different AZs)
2 Private Subnets (different AZs)


3. Configure Internet Connectivity:

Attach Internet Gateway to VPC
Create Route Tables:
Public subnets → Internet Gateway
Private subnets → NAT Gateway
5. Launch NAT Gateway
Deploy NAT Gateway in public subnet
Associate with private route table


6. Setup Security Groups
Allow:
HTTP (80) / HTTPS (443) from internet (ALB)
SSH (22) from trusted IP
Restrict database access to application layer only


8. Create Application Load Balancer
Internet-facing ALB
Attach to public subnets
Configure target group


10. Configure Auto Scaling Group
Launch Template with:
Amazon Linux / Ubuntu
Web server (Apache/Nginx)
Attach ASG to target group
Set min, desired, and max instances


11. Deploy RDS (Multi-AZ)
Choose engine (MySQL/PostgreSQL)
Enable Multi-AZ deployment
Place in private subnets


13. Deploy Application
SSH into EC2 or use User Data script
Install dependencies and deploy app
14. Test High Availability
Access application via ALB DNS
Simulate failure by stopping an instance


Verify traffic is routed to healthy instances
🔄 Fault Tolerance Features
Multi-AZ deployment ensures resilience against AZ failure
Auto Scaling replaces unhealthy instances
Load Balancer distributes traffic evenly
RDS Multi-AZ provides automatic failover
📊 Monitoring & Logging
Amazon CloudWatch for metrics and alarms
AWS CloudTrail for auditing
ALB access logs for traffic monitoring
🔐 Security Best Practices
Use least privilege IAM roles
Store secrets in AWS Secrets Manager
Enable HTTPS using SSL/TLS certificates
Regularly update and patch instances


🧪 Testing
Perform load testing using tools like Apache JMeter
Simulate AZ failure
Verify auto scaling and failover

Use CloudFront CDN for global performance

📜 License

This project is licensed under the MIT License.
