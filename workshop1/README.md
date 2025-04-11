# Workshop 1: Introduction to CI/CD with GitHub Actions

This directory contains the files and workflow for Workshop 1 of the CI/CD course. This workshop serves as a foundational introduction to version control with Git, GitHub, YAML configuration, and the basics of automation using GitHub Actions.

## Key Concepts Covered

*   **GitHub & Git Basics:** Understanding repositories, cloning, staging changes (`add`), saving changes (`commit`), and syncing with the remote repository (`push`, `pull`).
*   **YAML Fundamentals:** Basic syntax (indentation, key-value pairs, lists) used for configuring GitHub Actions.
*   **GitHub Actions Core Concepts:** Introduction to Workflows, Events (triggers like `push`, `pull_request`), Jobs, Runners (execution environments like `ubuntu-latest`), Steps, and Actions (reusable units like `actions/checkout`, `actions/setup-python`, `actions/upload-artifact`).
*   **Creating a Simple Workflow:** Building an automated process triggered by repository events.

## Practical Exercise Goal

The main exercise in this workshop involves creating a simple GitHub Actions workflow (`.github/workflows/workflow.yml` specific to this workshop/branch) that performs the following tasks:

1.  **Triggers** on specified events (e.g., `push` to this branch, `pull_request`, `workflow_dispatch`).
2.  **Runs** on a GitHub-hosted runner (e.g., `ubuntu-latest`).
3.  **Prints** a custom message including the user's name and the current date/time.
4.  **Sets up** a specific Python version.
5.  **Executes** the included Python script (`script.py`) which prints OS information.
6.  **Uploads** the output of the script as a build artifact.

### Files

*   `script.py`: The simple Python script executed by the workflow.
*   `README.md`: This file.

*(Note: The actual workflow definition resides in `.github/workflows/workflow.yml` and within the `workshop1` branch).*