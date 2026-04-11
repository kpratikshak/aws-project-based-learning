# 📅 AWS VPC — The Heart of AWS Networking 🌐 

**AWS VPC (Virtual Private Cloud)** is the foundation of all networking inside AWS.  
Every EC2 instance, database, load balancer, or container service you deploy **lives inside a VPC**. 

Understanding VPC = understanding how your entire cloud infrastructure communicates. 

---
    
## 🔥 Why VPC Is Essential 
 
- 🛡️ Designing secure architectures   
- 🌐 Creating public & private networks   
- 🚀 Enabling internet access with **Internet Gateway (IGW)** & **NAT Gateway**  
- 🔗 Connecting environments using **VPC Peering**  
- ⚙️ Building scalable DevOps deployments  

---

## 🎯 Why You Must Master VPC

Mastering VPC gives you full control over:

- Networking  
- Security boundaries  
- Traffic flow  
- Service-to-service connectivity  

VPC is one of the **most criti**


# AWS VPC, Subnets, IGW, NAT, Peering, SSH...

---

## ✅ Quick Summary (What You’ll Get)

- Create VPCs (Mumbai & Delhi) + Subnets  
- Attach Internet Gateway (IGW) + Public Route Table  
- Create NAT Gateway + Private Route Table  
- Create VPC Peering + routing both sides  
- Delete resources in correct order  
- PuTTYgen steps to convert PEM ↔ PPK  

---

# 1) Create a VPC (Example)

| Step | Action |
|------|--------|
| Console | VPC → Create VPC → **VPC only** |
| Name | `MyVPC01` |
| IPv4 CIDR | `10.0.0.0/24` (or `/16` for more IPs) |
| Result | VPC created |

---

# 2) Create Subnets

## Public Subnet (example)

| Field | Value |
|-------|-------|
| VPC | MyVPC01 |
| Name | `sub-public-1` |
| AZ | `ap-south-1a` |
| CIDR | `10.0.0.0/28` |
| Auto-assign public IPv4 | **Enable** |

## Private Subnet (example)

| Field | Value |
|-------|-------|
| VPC | MyVPC01 |
| Name | `sub-private-1` |
| CIDR | `10.0.1.0/28` |
| Auto-assign public IPv4 | **Disable** |

---

# 3) Internet Gateway (IGW) + Public Route Table

## Internet Gateway

| Step | Action |
|------|--------|
| Create | VPC → Internet Gateways → Create |
| Name | `igw-mumbai` |
| Attach | Attach to `MyVPC01` |

## Public Route Table

| Step | Action |
|------|--------|
| Create/Select | Route tables → `public-rt` |
| Add Route | `0.0.0.0/0` → Internet Gateway (`igw-mumbai`) |
| Associate | Public Subnet (`sub-public-1`) |

---

# 4) NAT Gateway (Private → Outbound Internet)

| Step | Action |
|------|--------|
| Create | NAT Gateway in **public subnet** (`sub-public-1`) |
| EIP | Allocate new Elastic IP |
| Result | NAT Gateway created |

## Private Route Table

| Route | Target |
|--------|--------|
| `0.0.0.0/0` | NAT Gateway |

Associate this route table with the private subnet (`sub-private-1`).

Outcome:  
Private EC2 → outbound internet OK, inbound blocked.

---

# 5) Security Groups (Recommended)

## Public EC2 SG

| Rule | Value |
|------|-------|
| Inbound | SSH (22) from **your IP** |
| Inbound | HTTP/HTTPS (80/443) from `0.0.0.0/0` (if web) |
| Outbound | All allowed |

## Private EC2 SG

| Rule | Value |
|------|-------|
| Inbound | From Public EC2 SG or ALB |
| Outbound | All allowed |

---

# 6) EC2 Deployment

## Public EC2
- Launch into `sub-public-1`
- Use Public-SG  
- This can serve as a **bastion/jump host**

## Private EC2
- Launch into `sub-private-1`
- Use Private-SG  
- SSH through bastion only

---

# 7) Create VPCs for Peering (Mumbai & Delhi)

---

## **Mumbai VPC**

| Item | Value |
|------|--------|
| VPC Name | `vpc-mumbai` |
| CIDR | `10.0.0.0/16` |
| Subnet | `sub1-mumbai` → `10.0.0.0/28` |
| IGW | `igw-mumbai` |
| Public RT | Route → `0.0.0.0/0 → igw-mumbai` |

---

## **Delhi VPC**

| Item | Value |
|------|--------|
| VPC Name | `vpc-delhi` |
| CIDR | `172.16.0.0/16` |
| Subnet | `sub1-delhi` → `172.16.0.0/28` |
| IGW | `igw-delhi` |
| Public RT | Route → `0.0.0.0/0 → igw-delhi` |

---

# 8) VPC Peering (Mumbai ↔ Delhi)

## Create Peering

| Step | Action |
|------|--------|
| Create | VPC → Peering Connections |
| Name | `my-peering` |
| Requester | `vpc-mumbai` |
| Accepter | `vpc-delhi` |

Accept request from the Delhi side.

## Add Routes (Both Sides)

### Mumbai Route Table
| Destination | Target |
|-------------|---------|
| `172.16.0.0/16` | Peering Connection |

### Delhi Route Table
| Destination | Target |
|-------------|---------|
| `10.0.0.0/16` | Peering Connection |

## Security Groups

Allow from peer CIDRs if required.

---

# 9) Deletion / Cleanup Order

| Order | Delete |
|--------|---------|
| 1 | Peering connection |
| 2 | EC2 Instances |
| 3 | NAT Gateway (release EIP) |
| 4 | Detach/Delete IGW |
| 5 | Subnets |
| 6 | Route Tables |
| 7 | VPC |

This avoids “resource in use” errors.

---

# 10) AWS Limits & Quotas

| Resource | Default Limit |
|----------|----------------|
| VPCs per Region | Usually 5 |
| Subnets | Large (no issue normally) |
| NAT Gateways | Limited by region, costly |

Request quota increase via **AWS Service Quotas**.

---

#AWS #DevOps #CloudComputing #AWSLearning #EBS #VolumeMounting #DataPersistence #LearningJourney #CareerGrowth #DevOpsEngineer #AWSCommunity
