# key : owners = ["Ashley", "Mike", "Alex", "Rodney"]
# value : dogs = ["Lily", "Bella", "Davey", "Lily", "Apollo"]

doggies = {"Bella": "Mike",
        "Lily": "Mike",
        "Lily": "Ashley",
        "Davey": "Alex",
        "Apollo": "Rodney"
        }

dogs = [
    {"name" : "Bella", "Breed" : "Silver Lab", "Age" : "11", "Owner" : "Mike"},
    {"name" : "Lily", "Breed" : "Black Lab", "Age" : "6", "Owner" : "Ashley"},
    {"name" : "Davey", "Breed" : "Golden Doodle", "Age" : "9", "Owner" : "Alex"},
]
for dog in dogs:
    print(dog["name"], dog["Age"], sep=", ")