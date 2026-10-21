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

issue_ids = [issue["id"] for issue in issues]

if issue_ids:
    print("List contains data")
    next_id = max(issue_ids) + 1
else:
    print("List is empty")
    next_id = 101

print(f"Existing IDs: {issue_ids}")
print(f"Next issue ID: {next_id}")

while True:
    title = input("Enter issue title: ").strip()

    if title:
        break
    print("Title cannot be empty. Please try again.")

valid_priorities = ["High", "Medium", "Low"]

while True:
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    if priority in valid_priorities:
        break
    print("Invalid priority. Please try again.")

new_issue = {
    "id": next_id,
    "title": title,
    "priority": priority,
    "resolved": False,
}

issues.append(new_issue)

print(f"Added issue: {new_issue['title']}")

print(f"Total issues: {len(issues)}")

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(issues, file, indent=4)

print("Issues saved successfully.")