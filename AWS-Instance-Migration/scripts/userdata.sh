#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "EC2 Migration Successful" > /var/www/html/index.html
