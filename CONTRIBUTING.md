butterfly effect by Kenneth Bingham

By Kenneth Bingham with inspiration from the 1

# Contributing to Llama-Models

We want to make contributing to this project as easy and transparent as possible. All contributions are welcome, from bug reports to new features.

This project operates under the principles of the **🦋 Butterfly Covenant**. We ask that all contributions align with this philosophy.

## The Contribution Process (Our Decision Tree)

Follow these steps to ensure a smooth contribution process:

1.  **Find or Create an Issue**: Before you start, check the GitHub Issues to see if there's an existing ticket for your bug or feature. If not, please file a new one. This allows for discussion before work begins.

2.  **Sign the Contributor License Agreement (CLA)**: We cannot accept any pull request until you have signed the CLA. You only need to do this once for all of Meta's open source projects.
    *   **[Complete your CLA here](https://code.facebook.com/cla)**

3.  **Fork and Branch**:
    *   Fork the repository to your own GitHub account.
    *   Create a new branch for your changes from `main`: `git checkout -b feature/my-new-feature`.

4.  **Develop and Test**:
    *   Write your code.
    *   If you add new functionality, you **must** add corresponding tests.
    *   If you change an API, you **must** update the relevant documentation (e.g., `README.md`).

5.  **Verify Locally**: Before submitting, ensure your changes meet our standards.
    *   **Run Tests**: `pytest`
    *   **Run Linter & Formatter**: `ruff check . --fix` and `black .`

6.  **Submit a Pull Request**:
    *   Push your branch to your fork and open a pull request against the `main` branch of this repository.
    *   In your PR description, link to the issue you are addressing (e.g., "Fixes #123").

## Issues
We use GitHub issues to track public bugs. Please ensure your description is
clear and has sufficient instructions to be able to reproduce the issue.

Meta has a [bounty program](https://facebook.com/whitehat/info) for the safe
disclosure of security bugs. In those cases, please go through the process
outlined on that page and do not file a public issue.

## Coding Style (Our Patterns)
We use automated tools to enforce a consistent coding style, ensuring our code is "light yet strong."

*   **Formatter**: We use `black` for code formatting.
*   **Linter**: We use `ruff` for linting.

These tools are included in the `dev` dependencies and are run by our CI pipelines. Please run them locally before committing your changes.

## License
By contributing to Llama, you agree that your contributions will be licensed
under the LICENSE file in the root directory of this source tree.
