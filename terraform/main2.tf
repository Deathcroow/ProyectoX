#esto quiero decir que version de terraform se va a crear
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
  backend "s3" {
    bucket = "mbacket1"
    key    = "path/to/my/key"
    region = "us-east-1"
  }
}

#definir y configurar el proveedor
provider "aws" {
  region     = "us-east-1"
  access_key = var.access_key
  secret_key = var.secret_key

}

resource "aws_instance" "example" {
  ami           = "ami-011899242bb902164" # Ubuntu 20.04 LTS // us-east-1
  instance_type = var.instance_type
  tags = {
    "Name" = "notfund"
  }
}
