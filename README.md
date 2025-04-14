[![CI/CD Pipeline AWS ECS con CloudFormation](https://github.com/sgalle16/cicd_course/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/sgalle16/cicd_course/actions/workflows/ci-cd.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
# CI/CD Course
## CI/CD Pipeline for Python Flask Web Application (AWS ECS Deployment)

This project contains the source code for a simple Flask web calculator application and its associated automated CI/CD pipeline. The pipeline handles testing, code analysis, containerization, and deployment to AWS Elastic Container Service (ECS) using Fargate and CloudFormation.

## Project Overview

*   **Application:** A basic web calculator built with Python and Flask.
*   **Pipeline Goal:** To fully automate the process from code commit to a running application in Staging and Production environments on AWS.

## Pipeline Summary

The workflow (`.github/workflows/ci-cd.yml`) orchestrates the following:

1.  **CI Phase (Workshop 2):**
    *   Code checkout, dependency installation.
    *   Linting (Pylint, Flake8) and Formatting checks (Black).
    *   Unit testing and code coverage (Pytest).
    *   Static code analysis (SonarCloud).
    *   Docker image build.
    *   Docker image push to Docker Hub (on `main` branch push).

2.  **CD Phase (Workshop 3):**
    *   Infrastructure deployment/update via CloudFormation to **Staging** environment on AWS ECS Fargate.
    *   Forcing ECS service update in Staging to pull the new image.
    *   Running acceptance tests (Selenium) against the **Staging** environment URL.
    *   Infrastructure deployment/update via CloudFormation to **Production** environment (only after Staging tests pass).
    *   Forcing ECS service update in **Production**.
    *   Running smoke tests (Selenium) against the **Production** environment URL.

## Technology Stack

*   **Language/Framework:** Python 3.12, Flask
*   **Testing:** Pytest, Coverage.py, Selenium
*   **Code Quality:** Black, Pylint, Flake8, SonarCloud
*   **Containerization:** Docker, Docker Hub
*   **CI/CD Platform:** GitHub Actions
*   **Cloud & Deployment:** AWS ECS, AWS CloudFormation, AWS CLI

## Directory Structure

*   `app/`: Source code for the Flask application.
*   `tests/`: Unit, acceptance, and smoke tests.
*   `template.yml`: AWS CloudFormation template for infrastructure.
*   `Dockerfile`: Defines the application's container image.
*   `.github/workflows/`: Contains the GitHub Actions workflow definition (`ci-cd.yml`).
*   *(Other config files: `requirements.txt`, `pytest.ini`, `sonar-project.properties`)*

### Further Details
For specifics on each phase, refer to:

*   [Workshop 1 Details](./workshop1/README.md)
*   [Workshop 2 Details (CI)](./cicd-pipeline-app/README_workshop2.md)
*   [Workshop 3 Details (CD)](./cicd-pipeline-app/README_workshop3.md)