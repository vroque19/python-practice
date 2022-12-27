# list of dicts
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter", "gender": "Female"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag", "gender": "Male"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrior", "gender": "Male"},
    {"name": "Draco", "house": "Slytherin", "patronus": None, "gender": "Male"}
]
# access to a whole collection of data
# iterate over a list of students
for student in students:
    print(student["name"], student["gender"], student["house"], sep=", ")
