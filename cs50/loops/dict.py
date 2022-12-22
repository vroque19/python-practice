# key : owners = ["Ashley", "Mike", "Alex", "Rodney"]
# value : dogs = ["Lily", "Bella", "Davey", "Lily", "Apollo"]

dogs = {"Bella": "Mike",
        "Lily": "Mike",
        "Lily": "Ashley",
        "Davey": "Alex",
        "Apollo": "Rodney"
        }
for dog in dogs:
    print(dog, dogs[dog], sep=", ")