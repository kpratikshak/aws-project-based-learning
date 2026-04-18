# AWS CloudWatch Monitoring 🚀

A comprehensive DevOps project demonstrating the setup and configuration of AWS CloudWatch for monitoring infrastructure and applications.

## 📖 Overview

In this project, we implement a robust monitoring solution using **AWS CloudWatch**. 
The setup involves tracking EC2 instances, managing logs, and creating active alerts to ensure high availability and performance of our infrastructure.

## 🎯 Key Features

- **Custom Dashboards:** Visualize system performance, resource utilization, and application metrics in a unified dashboard.
- **Metric Collection:** Monitor CPU, Memory, Disk I/O, and Network traffic.
- **Log Management:** Centralized logging using CloudWatch Logs with custom log groups and metric filters.
- **Automated Alarms:** SNS-integrated alerts for critical thresholds (e.g., CPU > 80%, Status Check Fails).
- **Auto Scaling Integration:** Dynamic scaling policies based on CloudWatch metrics.

## 📸 Screenshots

### CloudWatch Dashboard
![CloudWatch Dashboard](images/dashboard.png)
*A consolidated view of our infrastructure health, showing key metrics like CPU utilization and network traffic.*

### CloudWatch Alarm Configuration
![CloudWatch Alarm](images/alarm.png)
*An example of an active CloudWatch Alarm configured to trigger an SNS notification when a threshold is breached.*

## 🛠️ Architecture

1. **EC2 Instances** are provisioned with the CloudWatch Agent installed.
2. The agent collects system-level metrics and sends application logs to **CloudWatch Logs**.
3. **CloudWatch Metrics** aggregates the data, which is visualized on a **CloudWatch Dashboard**.
4. **CloudWatch Alarms** continuously evaluate metrics against predefined thresholds.
5. If an alarm state is triggered (e.g., `ALARM`), a notification is sent via **Amazon SNS** to the DevOps team.

## 🚀 Setup Instructions

### Prerequisites
- AWS Account
- IAM Role with CloudWatch permissions (`CloudWatchAgentServerPolicy`)
- AWS CLI configured locally

### 1. Install the CloudWatch Agent
Attach the IAM role to your EC2 instance and install the agent:
```bash
sudo yum install amazon-cloudwatch-agent -y
```

### 2. Configure the Agent
Run the configuration wizard to define which metrics and logs to collect:
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

### 3. Start the Agent
Apply the configuration and start the agent service:
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
```

## 📈 Monitoring Focus Areas

| Component | Metrics Tracked | Warning Threshold | Critical Threshold |
| :--- | :--- | :--- | :--- |
| **CPU** | `CPUUtilization` | 70% | 85% |
| **Memory** | `mem_used_percent` | 75% | 90% |
| **Disk** | `disk_used_percent` | 80% | 95% |
| **Network** | `NetworkIn` / `NetworkOut` | - | - |
| **Instance**| `StatusCheckFailed` | - | >= 1 |

## 🧹 Cleanup
To avoid incurring AWS charges, remember to:
- Terminate the EC2 instances.
- Delete CloudWatch Log Groups.
- Remove CloudWatch Alarms and Dashboards.

---
*Created as part of AWS Learning Project  focusing on modern infrastructure monitoring best practices.*
