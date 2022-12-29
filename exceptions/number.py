while True:
    try:
        x = int(input(("What is x? ")))
    except ValueError:
        print("x is not an integer.\n")
 #   else: # Name error: name 'x' is not defined ---> if passing in a non-integer into the int function results in a Value error,
 #                                                    meaning x never gets a value
 #       print(f"x is {x}")
    else:
        break

print(f"x is {x}")