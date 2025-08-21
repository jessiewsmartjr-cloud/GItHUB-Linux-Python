# AWS DevOps Automation Project

This repository contains:
- 📖 Jekyll documentation site (`/docs`)
- ⚙️ GitHub Actions CI pipeline
- 🧪 Python unit tests
- ☁️ Terraform and CloudFormation infrastructure templates
- 🧠 Lambda function source code

## Features

- Copy files between S3 buckets
- Parse logs and stream to Redshift or DynamoDB
- Trigger SageMaker ML training jobs via automation

## Usage

1. Deploy infrastructure using Terraform or CloudFormation.
2. Upload Lambda code to S3.
3. Configure event triggers (e.g., S3 PUT → Lambda).
4. Monitor logs via CloudWatch.

## Deployment Notes

- Enable GitHub Pages under `/docs` folder for live site.
- Pushes to main trigger CI tests via GitHub Actions.
