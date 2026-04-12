# 🚀 AWS EC2 Migration using Terraform

## 📌 Overview

This project demonstrates how to migrate and deploy an EC2 instance in AWS using Terraform Infrastructure as Code (IaC).

It provisions:

* EC2 instance
* Basic web server setup
* Modular Terraform structure

---

## 🧰 Prerequisites

* AWS Account
* Terraform installed
* AWS CLI configured (`aws configure`)
* SSH Key Pair in AWS

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/aws-ec2-migration-terraform.git
cd aws-ec2-migration-terraform
```

### 2. Initialize Terraform

```bash
terraform init
```

### 3. Configure Variables

Edit `terraform.tfvars`:

```hcl
ami_id   = "ami-xxxxxxxx"
key_name = "your-keypair"
```

### 4. Plan Deployment

```bash
terraform plan
```

### 5. Apply Configuration

```bash
terraform apply -auto-approve
```

---

## 🌐 Access Application

After deployment:

* Open browser
* Visit: `http://<EC2-Public-IP>`

---

## 🔄 Migration Strategy

This project simulates a **lift-and-shift migration**:

* Existing workload → EC2 instance
* Automated provisioning using Terraform
* Minimal configuration changes

---

## 🛡️ Disaster Recovery Strategies

### 1. Backup & Restore

* Use **AMI snapshots**
* Store backups in multiple regions

### 2. Multi-AZ Deployment

* Deploy EC2 instances across multiple Availability Zones
* Use Load Balancer for failover

### 3. Auto Scaling Group (ASG)

* Automatically replace failed instances
* Maintain desired capacity

### 4. Pilot Light Strategy

* Keep minimal infrastructure running
* Scale up during disaster

### 5. Warm Standby

* Fully functional but scaled-down environment
* Quick failover capability

### 6. Route 53 Failover Routing

* DNS-based failover mechanism

---

## 📤 Cleanup

```bash
terraform destroy -auto-approve
```

---

## 📌 Future Improvements

* Add VPC and Subnets
* Integrate Load Balancer
* Add Auto Scaling
* CI/CD pipeline (GitHub Actions)
* Remote backend (S3 + DynamoDB)

---

## 🤝 Contributing

Pull requests are welcome!

---

## 📜 License

MIT License
