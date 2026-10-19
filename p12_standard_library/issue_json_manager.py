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
print()


# Add new issue
print("-- Add new issue --")

new_issue = {
    "id": 102,
    "title": "Touch panel malfunction",
    "priority": "High",
    "resolved": False,
}

issue_exists = False

for issue in issues:
    if issue["id"] == new_issue["id"]:
        issue_exists = True
        break

if not issue_exists:
    issues.append(new_issue)
    print(f"Added issue: {new_issue['title']}")
else:
    print("Issue already exists.")

print(f"Total issues: {len(issues)}")

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(issues, file, indent=4)

print("Issues saved successfully.")