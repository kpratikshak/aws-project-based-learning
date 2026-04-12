variable "aws_region" {
  default = "ap-south-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ami_id" {
  description = "AMI ID for EC2"
}

variable "key_name" {
  description = "SSH Key Pair"
}
