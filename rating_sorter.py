import json

# 1. students.json faylini o‘qish
with open("students.json", "r") as file:
    students = json.load(file)

# 2. Score bo‘yicha kamayish tartibida saralash
students.sort(key=lambda x: x["score"], reverse=True)

# 3. Rank (o‘rin) qo‘shish
for i in range(len(students)):
    students[i]["rank"] = i + 1  # 1 dan boshlanadi

# 4. rating.json fayliga yozish
with open("rating.json", "w") as file:
    json.dump(students, file, indent=2)

