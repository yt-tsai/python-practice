# List example
line = "-------------------------"
names = [
    "Peter", 
    "Marina", 
    "Mika", 
    "PaiPai"
]

print(line)
print("List:")
print(names)
print("The second element in the list:")
print(names[1])

names.append("Kouso")

# Update data
names[2] = "Mikasukee"
# Update an element using its index.
# Incorrect for a list: names["Mika"] = "Mikasukee"

# Delete data
del names[1]            # Delete an element by index
names.remove("PaiPai")  # Delete an element by value

print(line)
print(names)
print(f"The length of current List:  {len(names)}")

print(line)

for name in names:
    print(name)