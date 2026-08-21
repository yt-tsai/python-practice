language = 'Python'
study_hours = 25

if study_hours >= 30:
    level = 'Advanced'
elif study_hours >= 15:
    level = 'Intermediate'
else:
    level = 'Beginner'

print(f'''
Language: {language}
Study Hours: {study_hours}
Level: {level}
''')