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
  access_key = "AKIA2NIW2JQV2YYP4T4Z"
  secret_key = "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"

}

variable "instance_type" {
  type        = string
  description = "Instance type"
  default     = "t2.micro"

}

resource "aws_instance" "example" {
  ami           = "ami-011899242bb902164" # Ubuntu 20.04 LTS // us-east-1
  instance_type = var.instance_type
  tags = {
    "Name" = "Instancias_Terraform"
  }
}
