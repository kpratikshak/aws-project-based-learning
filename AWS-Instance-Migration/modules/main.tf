resource "aws_instance" "ec2" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name

  user_data = file("${path.module}/../../scripts/user_data.sh")

  tags = {
    Name = "Migration-Instance"
  }
}
