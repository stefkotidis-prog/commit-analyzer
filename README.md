# GitHub Commit Analyzer 

A Python script that extracts and analyzes commit messages from a GitHub repository using the GitHub REST API.

## Overview
This script fetches the 100 most recent commits from a public repository (currently configured for `AutoGPT`). It uses `pandas` to categorize the commits into four main groups based on specific keywords:
* **Bug Fixes** (`fix`, `bug`, `error`, etc.)
* **New Features** (`feat`, `add`, `implement`, etc.)
* **Documentation** (`docs`, `readme`, etc.)
* **Refactoring & Maintenance** (`refactor`, `clean`, etc.)

After processing the data, it uses `matplotlib` to generate a bar chart (`commit_taxonomy_chart.png`) visualizing the distribution of the commit categories.

## Prerequisites
* Python 3.x

## Installation & Usage
1. Clone this repository or download the files.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate  
   
   # On Windows:
   venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python analyzer.py
   ```
