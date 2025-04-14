# Workshop 3: Continuous Deployment to AWS ECS

This part of the project extended the CI pipeline to implement **Continuous Deployment (CD)**, deploying the application to AWS.

## Goal

To automate the deployment of the Docker image (built in Workshop 2) to Staging and Production environments running on AWS Elastic Container Service (ECS) using Infrastructure as Code (IaC).

## Key Pipeline Stages Implemented

*   **Infrastructure as Code (IaC):** Defined AWS infrastructure using CloudFormation (`template.yml`).
*   **Staging Deployment:** Automated deployment to an ECS Fargate Staging environment via CloudFormation.
*   **Staging Testing:** Ran Selenium acceptance tests against the live Staging environment.
*   **Production Deployment:** Automated deployment to an ECS Fargate Production environment via CloudFormation after successful Staging validation.
*   **Production Smoke Testing:** Ran basic Selenium smoke tests against the live Production environment.

## Outcome

A full CI/CD pipeline where validated code changes are automatically deployed through Staging and into Production environments on AWS ECS, managed declaratively.

## Relevant Files Added/Modified

*   `template.yaml` (CloudFormation IaC definition)
*   `tests/test_smoke_app.py` (Production smoke tests)
*   `.github/workflows/ci-cd.yml` (Final workflow including CD stages)