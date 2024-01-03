#esto quiero decir que version de terraform se va a crear
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

#definir y configurar el proveedor
provider "aws" {
  region     = "us-east-1"

}

resource "aws_instance" "example" {
  ami              = "ami-011899242bb902164" # Ubuntu 20.04 LTS // us-east-1
  instance_type    = "t2.micro"
  tags = {
    "Name" = "terra2" 
  }
}
