nutrition = {
    "Apple" : "130",
    "Sweet Cherries" : "100",
    "Avacado" : "50",
}

fruit = input("Apple, Sweet Cherries, or Avacado?\n")

print("Calories: " + nutrition[fruit.lower().capitalize()])