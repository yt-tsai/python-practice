# Dictionary
line = "-------------------------"
print(line)

countries = {
    "JP": "Japan", 
    "TW": "Taiwan", 
    "US": "United States"
}

print(countries)

print(countries["JP"], countries["TW"])
print(len(countries))

print(line)
countries["KR"] = "South Korea"
countries["JP"] = "JAPAN (updated)"
print(countries)
print(len(countries))

print(line)
del countries["US"]
print(countries)
print(len(countries))

print(line)
print(countries.get("PAIPAI"))
print(countries.get("JP"))

print(line)
print("JP" in countries)
print("US" in countries)

print(line)
for key in countries:
    print(f"{key} : {countries[key]}")
