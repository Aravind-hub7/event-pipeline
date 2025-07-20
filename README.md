# Event-Driven Data Pipeline on AWS using Terraform

This project sets up an event-driven data pipeline on AWS using:
- 🗃️ S3 for data storage
- 🧠 AWS Lambda for processing
- 🔒 IAM Roles for security
- 🔁 Terraform for Infrastructure as Code
- 🚀 GitHub Actions for CI/CD

## How It Works

1. Terraform deploys the required AWS infrastructure.
2. A Lambda function gets triggered and stores events in S3.
3. GitHub Actions automates deployment on every push.

## Files in This Repo

- `main.tf` – Terraform config
- `lambda_function.py` – AWS Lambda code
- `lambda_function_payload.zip` – Packaged Lambda
- `variables.tf` – Optional variables
- `.github/workflows/` – GitHub Actions config

 ## Deployment Steps

 ```bash
 # Deploy infrastructure
    terraform init
    terraform apply

    ## Cleanup (Optional)

    To remove all AWS resources created by this project:

    ```bash
    terraform destroy -auto-approve
    ⚠️ WARNING: This will delete the Lambda function, S3 bucket, IAM roles, and all data.

    


