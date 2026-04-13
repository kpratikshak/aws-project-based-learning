What Is AWS Auto Scaling?

AWS Auto Scaling automatically adjusts the number of EC2 instances running in your application based on demand. When traffic increases, Auto Scaling adds more instances. When traffic decreases, it removes extra instances.

 

When more people arrive, more guards are added
When people leave, extra guards go home
The event runs smoothly without waste
Moving forward, in a previous post, we created an Amazon EC2 instance to run an application. As we progress, we will build on that setup and extend it by configuring AWS Auto Scaling.

Setting Up AWS Auto Scaling (Step by Step)
Step 1: Confirm Your EC2 Instance Is Running
Before setting up Auto Scaling:

Go to EC2 → Instances
Ensure your EC2 instance created earlier is running
Confirm it has:

A working application
A security group allowing required traffic (for example, HTTP on port 80)
This EC2 instance will be used as the base for Auto Scaling.

Step 2: Create an Auto Scaling Group
Click Auto Scaling Groups
 

Click Create Auto Scaling group
 

Enter a name
Select the launch template
 

Click Next
Step 3: Choose Network Settings
Select your VPC
Choose at least two subnets
 

Click Next
This improves availability.

Step 4 Attach a Load Balancer (Recommended)
Choose Attach to a new load balancer
Select Application Load Balancer
Enable Health checks
 

 

Step 6: Configure Scaling Policy
This tells AWS when to scale.

Choose Target tracking scaling
Metric: Average CPU utilization
Target value: 50%
y.



 


 

What Just Happened?
You started with one EC2 instance
Auto Scaling now launches identical EC2 instances when needed
Extra instances are removed when traffic drops
User traffic reaches the Load Balancer → traffic is shared across EC2 instances → Auto Scaling monitors CPU usage → new instances are added when demand increases → unused instances are removed when demand drops.

When Should You Use Auto Scaling?
Use Auto Scaling when:

Traffic is unpredictable
Need of high availability
You want to reduce costs
You don’t want to manage servers manually
