# menu dict
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# set total amount to 0
total_amount = 0

# infinite loop
while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            total_amount += menu[item]
            print("Total: $", end=" ")
            print("{:.2f}".format(total_amount))
    except EOFerror:
        break

# exception