# GitHub Commit Analyzer

A Python script that extracts and analyzes commit messages from a GitHub repository using the GitHub REST API.

## Overview
This script fetches the most recent commits from a specified public repository (currently only configured for `AutoGPT`) and calculates the proportion of commits dedicated to bug fixing, based on specific keywords (`fix`, `bug`, `error`). It filters the JSON response data and counts commits containing the specific keywords mentioned above.

## Prerequisites
* Python 3.x
* `requests` library

## Installation & Usage
1. Clone this repository or download the `analyzer.py` file.
2. Install the required dependency:
   ```bash
   pip install requests
