# AWS Elastic File System (EFS) - Shared Storage Guide ☁️📁

I learned how to create, configure, and mount an Amazon EFS (Elastic File System) to multiple EC2 instances simultaneously to provide centralized, shared data storage. This is extremely useful in real DevOps environments where scalable web applications or distributed systems need to read and write to the same file system at the same time.

## 👉 Key Things I Learned

| Concept :

| **EFS Importance** | Provides highly scalable, fully managed, and centralized shared file storage for EC2 instances. |
| **File-Level Storage** | Uses the NFSv4 (Network File System) protocol, allowing concurrent access from thousands of instances. |
| **Multi-AZ Availability** | Data is stored redundantly across multiple Availability Zones, ensuring high availability and durability. |
| **True Elasticity** | Storage capacity automatically grows and shrinks as files are added/removed. No need to pre-provision disk size! |
| **Security Groups (NFS)** | EFS requires an inbound security group rule for NFS (Port 2049) to allow EC2 instances to connect safely. |
| **Mount Helper** | The `amazon-efs-utils` tool simplifies the mounting process and optimizes performance. |
| **Best Use Cases** | Ideal for Content Management Systems (like WordPress), data analytics, ML datasets, and shared CI/CD pipelines. |

---

## 📌 AWS EFS Shared Storage – Step-by-Step Guide

**Topic:** How to create, mount, and share an EFS File System across multiple AWS EC2 instances.

### 🚀 What You Will Learn
* Create an Elastic File System (EFS).
* Configure Security Groups for NFS traffic (Port `2049`).
* Mount the EFS volume inside multiple Linux EC2 instances.
* Store data on Server A and verify it instantly appears on Server B.

---

### 🏗 Step 1: Create EC2 Instances
Launch **two** Linux EC2 instances (Amazon Linux 2023 / Ubuntu) in the same VPC. We will use two instances to demonstrate how EFS shares data across multiple servers.

### 🛡 Step 2: Configure Security Groups
EFS needs permission to talk to your EC2 instances.
1. Go to **EC2 → Security Groups** and locate the Security Group attached to your EFS.
2. Edit **Inbound Rules**.
3. Add Rule:
   * **Type:** `NFS`
   * **Port Range:** `2049`
   * **Source:** Select the Security Group ID of your EC2 instances.

### 💽 Step 3: Create an EFS File System
1. Go to: **EFS → File Systems → Create file system**
2. Click **Customize** (or use the quick create):
   * **Name:** `MySharedEFS`
   * **VPC:** Must match the VPC of your EC2 instances.
   * **Storage Class:** Regional *(Recommended for multi-AZ availability)*.
3. Click **Create** and wait for the status to become `Available`.
4. Note down the **File System ID** *(Example: `fs-0123456789abcdef0`)*.

---

### 🔗 Step 4: Mounting The EFS in Linux (Server A)

Connect to your first EC2 instance via SSH.

**1. Install the EFS Mount Helper** *(Pre-installed on some Amazon Linux AMIs, but good to verify)*
```bash
sudo yum install -y amazon-efs-utils

## Check my advanced project:
 AWS EFS Analyzer with Python:  https://github.com/kpratikshak/aws-efs-analyzer/tree/main
