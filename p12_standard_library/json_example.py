import json


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
