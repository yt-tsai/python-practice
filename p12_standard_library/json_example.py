import json
from pathlib import Path


# JSON dumps basics
print("-- JSON dumps basics --")

issue = {
    "id": 101,
    "title": "Login error",
    "priority": "High",
    "resolved": False,
}

json_text = json.dumps(issue, indent=4)

print(json_text)
print(type(issue))
print(type(json_text))
print()


# JSON loads basics
print("-- JSON loads basics --")

parsed_issue = json.loads(json_text)

print(f"Issue ID: {parsed_issue['id']}")
print(f"Title: {parsed_issue['title']}")
print(f"Priority: {parsed_issue['priority']}")
print(f"Resolved: {parsed_issue['resolved']}")
print(f"Type: {type(parsed_issue)}")
print()


# JSON dump to file
print("-- JSON dump to file --")

file_path = Path(__file__).parent / "issues.json"

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(issue, file, indent=4)

print(f"JSON file saved: {file_path}")
