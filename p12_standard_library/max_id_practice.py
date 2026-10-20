issues = [
    {"id": 101, "title": "Login error"},
    {"id": 102, "title": "Touch panel malfunction"},
    {"id": 105, "title": "Network timeout"},
]

# issue_ids = []
# for issue in issues:
#     issue_ids.append(issue["id"])

issue_ids = [issue["id"] for issue in issues]

if issue_ids:
    print("List contains data")
    next_id = max(issue_ids) + 1
else:
    print("List is empty")
    next_id = 101

print(f"Existing IDs: {issue_ids}")
print(f"Next issue ID: {next_id}")