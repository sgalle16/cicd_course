# Workshop 2: Continuous Integration Pipeline Python

This part of the project focused on building the **Continuous Integration (CI)** pipeline for the Python Flask web application.

## Goal

To automate the process of building, testing, and analyzing the code quality, culminating in the creation of a distributable Docker image.

## Key Pipeline Stages Implemented

*   **Code Formatting & Linting:** Used Black, Pylint, and Flake8 for code style and static analysis.
*   **Unit Testing:** Ran automated unit tests using Pytest and measured code coverage.
*   **Static Analysis (SonarCloud):** Integrated SonarCloud for deeper code quality and security checks.
*   **Acceptance Testing:** Performed automated browser tests with Selenium against a locally running instance.
*   **Docker Image Build:** Created a container image using the `Dockerfile`.
*   **Docker Image Push:** Published the built image to Docker Hub upon successful validation on the `main` branch.

## Outcome

A GitHub Actions workflow that validates code changes and automatically produces a versioned Docker image in Docker Hub, ready for the next stage (deployment).

## Relevant Files

*   `app/`, `tests/` 
*   `Dockerfile`, `requirements.txt`, `pytest.ini`, `sonar-project.properties`
*   Initial version of `.github/workflows/ci.yml` (later evolved into `ci-cd.yml`)