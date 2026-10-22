import json
from pathlib import Path

file_path = Path(__file__).parent / "manager_issues.json"

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        issues = json.load(file)
else:
    issues = []

while True:
    print("\n===== Issue JSON Manager =====")
    print("1. View issues")
    print("2. Add issue")
    print("3. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        print("-- Issue List --")

        if issues:
            for issue in issues:
                print(f"ID: {issue['id']} | {issue['priority']} | {issue['title']}")
            print()
            print(f"Total issues: {len(issues)}")
        else:
            print("No issues found.")

    elif choice == "2":
        print("-- Add New Issue --")

        issue_ids = [issue["id"] for issue in issues]

        if issue_ids:
            print("List contains data")
            next_id = max(issue_ids) + 1
        else:
            print("List is empty")
            next_id = 101

        print(f"Next issue ID: {next_id}")

    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option. Please try again.")