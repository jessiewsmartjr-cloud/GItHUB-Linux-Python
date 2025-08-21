
variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
  default     = "my-automation-bucket"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "logProcessor"
}
