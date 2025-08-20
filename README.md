[![Build](https://img.shields.io/github/actions/workflow/status/jwsmart/ibm/python-ci.yml?branch=main)](https://github.com/jwsmart/ibm/actions)
[![Last Commit](https://img.shields.io/github/last-commit/jwsmart/ibm)](https://github.com/jwsmart/ibm/commits/main)
[![License](https://img.shields.io/github/license/jwsmart/ibm)](LICENSE)
[![Issues](https://img.shields.io/github/issues/jwsmart/ibm)](https://github.com/jwsmart/ibm/issues)
[![Stars](https://img.shields.io/github/stars/jwsmart/ibm?style=social)](https://github.com/jwsmart/ibm/stargazers)

# AWS Automation Toolkit

A comprehensive, multi-service AWS automation toolkit using Python and infrastructure-as-code (IaC). Includes hands-on scripts, templates, and testing framework.

## 🚀 Features

- Move files between S3 buckets
- Parse logs and push to DynamoDB or Redshift
- Trigger ML training jobs with SageMaker
- Terraform IAM role automation
- CloudFormation DynamoDB + Lambda deployment
- Jupyter Notebook and Python script versions
- Unit tests and CI/CD pipeline with GitHub Actions

## 🧪 Testing

Uses `pytest` to validate AWS automation logic with mock dependencies.

```bash
pytest tests/
```

## 📦 Setup

1. Clone the repo
2. Create a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📂 Folder Structure

- `scripts/` - Python scripts for AWS tasks
- `notebooks/` - Jupyter version of automation
- `templates/` - Terraform and CloudFormation IaC
- `docs/` - PDF guides and text walkthroughs
- `samples/` - Log file examples
- `tutorial/` - Teaching and video script
- `tests/` - Unit tests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
