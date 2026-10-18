import json
from pathlib import Path


# Issue JSON Manager
print("-- Issue JSON Manager --")

file_path = Path(__file__).parent / "manager_issues.json"

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        issues = json.load(file)
else:
    issues = []

print(f"Issues: {issues}")
print(f"Total issues: {len(issues)}")