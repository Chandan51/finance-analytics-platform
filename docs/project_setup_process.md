# Finance Analytics Platform — Project Setup Process

## 1. Project Folder Structure

### Purpose
Create a clean separation between notes, code, data, documentation, and future tools.

### Current structure

```text
OneDrive/
└── financialanalytics/
    ├── Finance Analytics Platform/          # Obsidian notes and learning documentation
    └── Github/
        └── finance-analytics-platform/      # GitHub repository / code project

2. Navigate to Project Repository

cd ~/OneDrive/financialanalytics/Github/finance-analytics-platform

Definition: Moves terminal into the main project repository folder.

pwd

Definition: Shows the current folder path to confirm you are in the correct location.

3. Check Python Version
python3 --version

Definition: Confirms Python is installed and shows the active Python version.

4. Create Virtual Environment
python3 -m venv venv

Definition: Creates an isolated Python environment inside the project folder.

5. Activate Virtual Environment
source venv/bin/activate

Definition: Activates the project-specific Python environment.

Expected terminal prefix:

(venv)
6. Install Core Python Libraries
pip install pandas numpy matplotlib jupyter sqlalchemy

Definition: Installs the first required Python packages for data analysis and project work.

7. Save Installed Libraries
pip freeze > requirements.txt

Definition: Saves all installed Python packages into requirements.txt so the environment can be recreated later.

8. Create Script Folder Structure
mkdir -p scripts/data_ingestion scripts/transformations scripts/analysis scripts/utilities

Definition: Creates organized folders for Python scripts.

Folder meaning
scripts/data_ingestion      # Scripts to collect or import data
scripts/transformations     # Scripts to clean or transform data
scripts/analysis            # Scripts for analysis and exploration
scripts/utilities           # Reusable helper functions
9. Verify Folder Creation
ls scripts

Definition: Lists folders inside the scripts directory.

Expected output:

analysis
data_ingestion
transformations
utilities
10. Create First Python Test Script
touch scripts/analysis/test_setup.py

Definition: Creates an empty Python file to test if the environment works.

11. Test Script Content
import pandas as pd
import numpy as np

print("Environment working successfully")

data = {
    "stock": ["AAPL", "MSFT", "SAP"],
    "price": [210, 430, 265]
}

df = pd.DataFrame(data)

print(df)

Definition: Tests whether Python, pandas, and numpy are working correctly.

12. Run Python Test Script
python scripts/analysis/test_setup.py

Definition: Executes the Python script from the terminal.

Expected output:

Environment working successfully

  stock  price
0  AAPL    210
1  MSFT    430
2   SAP    265
13. Git Commit Process
git status

Definition: Shows which files have changed.

git add .

Definition: Stages all changed files for commit.

git commit -m "Configured Python environment and initial script structure"

Definition: Saves a meaningful project checkpoint locally.

git push

Definition: Uploads committed changes to GitHub.

14. Important Lessons Learned
Folder diagrams are not terminal commands.
Always use pwd to confirm location before running commands.
Use a virtual environment for every Python project.
requirements.txt makes the setup repeatable.
Every meaningful setup step should be documented.
Every work session should end with documentation or a Git commit.


15. Current Project Status

Completed:

GitHub repository created
Project folders created
Python virtual environment created
Core Python libraries installed
Requirements file generated
Script folder structure created
First Python test script executed successfully

Next:

Commit setup work to GitHub
Start financial data ingestion pipeline

Then commit it:

```bash
git add docs/project_setup_process.md requirements.txt scripts/
git commit -m "Added project setup process documentation"
git push

This is exactly the habit we want: every technical movement becomes reusable knowledge.