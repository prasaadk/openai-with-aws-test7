# openai-with-aws-test7

This repository demonstrates how to provision AWS infrastructure using Terraform and GitHub Actions. It creates:

- An S3 bucket called `ontoscale-create-with-openai-codex`.
- A Lambda function exposed through API Gateway that writes a file into the bucket.

Terraform state is stored in the S3 bucket `ontoscale-terraform-backend`.

## GitHub Actions

Two workflows are provided:

- **Deploy** (`.github/workflows/deploy.yml`) – runs on merges to `main` and applies the Terraform configuration using the `AWS_ROLE` secret.
- **Destroy** (`.github/workflows/destroy.yml`) – can be triggered manually to tear down all resources.

## Usage

1. Commit changes and merge to `main` to trigger deployment.
2. Trigger the Destroy workflow manually from the Actions tab when you want to remove the infrastructure.

