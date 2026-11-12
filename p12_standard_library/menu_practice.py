import json
from pathlib import Path

file_path = Path(__file__).parent / "manager_issues.json"

# Get issue ID
def get_issue_id():
    try:
        issue_id = int(input("Enter issue ID: "))
        return issue_id
    except ValueError:
        print("Invalid issue ID. Please enter a number.")
        return None


# Get valid issue priority
def get_priority():
    valid_priorities = ["High", "Medium", "Low"]

    while True:
        priority = input(
            "Enter priority (High/Medium/Low): "
        ).strip().capitalize()

        if priority in valid_priorities:
            return priority

        print("Invalid priority. Please try again.")


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
    priority = get_priority()

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


# Update an issue
def update_issue(issues, file_path):

    issue_id = get_issue_id()

    if issue_id is None:
        return

    for issue in issues:
        if issue["id"] == issue_id:
            print(f"Found: {issue['title']}")
            print(f"Current priority: {issue['priority']}")

            print("1. Update title")
            print("2. Update priority")

            update_choice = input("Select an option: ").strip()

            if update_choice == "1":
                while True:
                    title = input("Enter issue title: ").strip()

                    if title:
                        break

                    print("Title cannot be empty. Please try again.")

                issue["title"] = title
                save_issues(issues, file_path)
                print("Title updated successfully.")
                return
                
            elif update_choice == "2":
                priority = get_priority()

                issue["priority"] = priority
                save_issues(issues, file_path)
                print("Priority updated successfully.")
                return

            else:
                print("Invalid option. Please try again.")
                return

    print("Issue not found.")


# Delete an issue
def delete_issue(issues, file_path):

    issue_id = get_issue_id()

    if issue_id is None:
        return

    for issue in issues:
        if issue["id"] == issue_id:
            print(f"Found: {issue['title']}")

            confirmation = input("Are you sure? (Y/N): ").strip().upper()

            if confirmation == "Y":
                issues.remove(issue)
                save_issues(issues, file_path)
                print("Issue deleted successfully.")
            elif confirmation == "N":
                print("Cancelled.")
            else:
                print("Invalid option. Please try again.")

            return
    
    print("Issue not found.")


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
    print("3. Update issue")
    print("4. Delete issue")
    print("5. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        view_issues(issues)

    elif choice == "2":
        add_issue(issues, file_path)

    elif choice == "3":
        update_issue(issues, file_path)

    elif choice == "4":
        delete_issue(issues, file_path)

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid option. Please try again.")