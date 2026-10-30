import json
from pathlib import Path

file_path = Path(__file__).parent / "manager_issues.json"


# Display issues
def view_issues(issues):
    print("-- Issue List --")

    if issues:
        for issue in issues:
            print(f"ID: {issue['id']} | {issue['priority']} | {issue['title']}")
        print()
        print(f"Total issues: {len(issues)}")
    else:
        print("No issues found.")


# Save issues to JSON
def save_issues(issues, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(issues, file, indent=4)


# Add an issue
def add_issue(issues, file_path):
    print("-- Add New Issue --")

    # Calculate next issue ID
    issue_ids = [issue["id"] for issue in issues]

    if issue_ids:
        next_id = max(issue_ids) + 1
    else:
        next_id = 101

    print(f"Next issue ID: {next_id}")

    # Title input
    while True:
        title = input("Enter issue title: ").strip()

        if title:
            break
        print("Title cannot be empty. Please try again.")

    # Priority input
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
        "resolved": False
    }

    issues.append(new_issue)

    print(f"Total issues: {len(issues)}")

    save_issues(issues, file_path)

    print("Issues saved successfully.")


# Load
def load_issues(file_path):
    # Read JSON and return the issues list
    if file_path.exists():
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error: Failed to load {file_path.name}: {e}")
            raise

    return []


issues = load_issues(file_path)


# Main menu
while True:
    print("\n===== Issue JSON Manager =====")
    print("1. View issues")
    print("2. Add issue")
    print("3. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        view_issues(issues)

    elif choice == "2":
        add_issue(issues, file_path)

    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option. Please try again.")