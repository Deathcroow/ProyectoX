variable "instance_type" {
  type        = string
  description = "Instance type"
  default     = "t2.micro"

}

variable "access_key" {
  type        = string
  description = "access_key"
  default     = ""

}

variable "secret_key" {
  type        = string
  description = "secret_key"
  default     = ""
}
