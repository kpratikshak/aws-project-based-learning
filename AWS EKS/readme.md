Building Web Applications Using Amazon EKS:
🚀Features:
This project demonstrates the deployment of a highly scalable, resilient web application using Amazon EKS (Elastic Kubernetes Service). The architecture leverages a Microservices Architecture (MSA) involving Flask and Node.js backends with a React frontend, managed through modern DevOps practices including CI/CD automation, serverless computing with AWS Fargate, and robust monitoring via CloudWatch Container Insights.

🏗 Architecture
The architecture consists of:

Amazon EKS: Managed Kubernetes cluster for orchestration.

AWS Fargate: Serverless compute for containers, reducing overhead.

Application Load Balancer (ALB): Managed via the AWS Load Balancer Controller for external traffic.

Amazon ECR: Private registry for Docker images.

CloudWatch Container Insights: Monitoring and logging using Fluent Bit.

🛠 Tech Stack
Orchestration: Kubernetes (Amazon EKS)

Compute: AWS Fargate & EC2

CI/CD: GitHub Actions & ArgoCD

IaC: eksctl & YAML Manifests

Monitoring: CloudWatch, Container Insights, Fluent Bit

Languages: Python (Flask), Node.js (Express), JavaScript (React)

🔧 Implementation Steps
1. Cluster Provisioning
The cluster is provisioned using eksctl with a configuration file to define managed node groups and IAM policies.

Bash
eksctl create cluster -f eks-demo-cluster.yaml
2. AWS Load Balancer Controller Setup
To handle Ingress resources, the AWS Load Balancer Controller is installed. It integrates with IAM Roles for Service Accounts (IRSA).

3. Microservices Deployment
The application is split into three main components:

Flask Backend: Handles data processing.

Node.js Backend: Manages service logic.

React Frontend: Deployed on AWS Fargate for serverless scaling.

4. GitOps CI/CD Pipeline
The project implements a GitOps workflow:

Developer pushes code to the App repo.

GitHub Actions builds the image, scans it with Trivy, and pushes to ECR.

Kustomize updates the image tag in the Manifest repo.

ArgoCD detects the change and synchronizes the cluster state.

📈 Monitoring & Scaling
HPA: Automatically scales Pods based on CPU utilization.

Cluster Autoscaler: Adds/removes EC2 nodes based on pending Pods.

Container Insights: Provides a tree-view map of cluster health.

📸 Generated Project Visuals
To enhance your GitHub repository, I have generated relevant screenshots/diagrams based on your project content:

1. System Architecture Diagram
This illustrates the flow from the user through the ALB into the EKS cluster.

2. CI/CD GitOps Workflow
This visualizes the automated pipeline described in your implementation.

3. Monitoring Dashboard Concept
A representation of what Container Insights looks like for this specific application.

