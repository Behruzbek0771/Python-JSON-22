import json

with open("students.json", "r") as file:
    students = json.load(file)

students.sort(key=lambda x: x["score"])

for i in range(len(students)):
    students[i]["rank"] = i + 1

with open("rating.json", "w") as file:
    json.dump(students, file, indent=2)
