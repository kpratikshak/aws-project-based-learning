🚀 Provisioning a Highly Available Amazon Aurora Cluster
Learn how to deploy a managed, MySQL-compatible relational database using Amazon Aurora. This guide covers security configuration, provisioning, and connectivity verification.

📊 Project Overview:
Cloud Provider: AWS

Cost: Aurora is not eligible for the AWS Free Tier.
Approx cost: $0.29/hr (for db.r5.large in US-East-1).

🛠 Prerequisites
An active AWS Account.

A local SQL Client (e.g., MySQL Workbench, Sequel Ace, or DBeaver).

Phase 1: Security Configuration
Before creating the database, we must define the firewall rules (Security Groups) to allow traffic on port 3306.

Navigate to the VPC Dashboard in the AWS Console.

Click on Security Groups > Create security group.

Basic Details:

Name: aurora-public-access-sg

Description: Allow MySQL access from my local IP.

VPC: Select your Default VPC.

Inbound Rules:

Type: MySQL/Aurora

Protocol: TCP | Port Range: 3306

Source: 0.0.0.0/0 (⚠️ Note: For production, always use "My IP").

Click Create security group.

Phase 2: Provisioning the Aurora Cluster
Navigate to the RDS Dashboard and click Create database.

Creation Method: Select Standard create.

Engine options:

Engine type: Amazon Aurora

Edition: Amazon Aurora with MySQL compatibility.

Templates: Select Dev/Test (optimal for testing and cost-control).

Settings:

DB cluster identifier: my-aurora-project

Master username: admin

Master password: [Your Password]

Instance configuration:

Select db.r5.large (or db.r6g.large for better price/performance in 2026).

Connectivity:

Public access: Select Yes.

Existing VPC security groups: Remove default and add aurora-public-access-sg.

Scroll to the bottom and click Create database. This typically takes 5–10 minutes to provision.

Phase 3: Connectivity and Verification
Once the status is Available, click on your DB cluster identifier.

In the Connectivity & security tab, find the Endpoints section.

Copy the Writer endpoint address.

Open your SQL Client and create a new connection:

Host: [Paste Writer Endpoint]

User: admin | Port: 3306

Run Test Query:

SQL
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE hardware_inventory (id INT, item_name VARCHAR(50));
INSERT INTO hardware_inventory VALUES (1, 'Ceph Node'), (2, 'Prometheus Server');
SELECT * FROM hardware_inventory;
Phase 4: Clean Up (Crucial)
To avoid being billed for idle resources, delete the cluster immediately after testing.

Select your database in the RDS console.

Go to Actions > Delete.

IMPORTANT: If the delete option is greyed out, click Modify, scroll to the bottom, uncheck Enable deletion protection, and save.

In the Delete prompt: Uncheck "Create final snapshot" and acknowledge the deletion.

🧠 Knowledge Check
1. What type of database is Aurora?
It is a cloud-native, managed relational database service (RDBMS). It is designed to be "decoupled," meaning compute and storage scale independently.

2. What are the storage limits in 2026?
The storage starts at 10 GB and automatically scales in 10 GB increments up to 128 TB. You only pay for the storage you actually use.

3. Standard vs. Serverless v2?

Standard (Provisioned): You choose a fixed instance size (like db.r5.large). Best for predictable workloads.

Serverless v2: Scales capacity (measured in ACUs) instantly based on application demand. Ideal for variable or spikey traffic.

4. How does data redundancy work?
Aurora replicates your data 6 times across 3 Availability Zones (AZs). It can lose up to two copies of data without affecting write availability and up to three copies without affecting read availability.

5. What are the primary Endpoints?

Writer Endpoint: Maps to the primary instance (handles Reads/Writes).

Reader Endpoint: Load-balances traffic across available Read Replicas.

6. Why is "Public Access" generally discouraged?
Enabling Public Access exposes your database port to the open internet. In a professional architecture, databases reside in Private Subnets, and developers connect via a Bastion Host (Jump Box) or AWS Client VPN.
