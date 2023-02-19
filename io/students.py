import csv

students = []
# DictReader returns dictionaries
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name" : name, "home" : home}
#         students.append(student)

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['home']}")

