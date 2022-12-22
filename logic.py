# logical operators (and, or, not)

temp = int(input("What is the temperature outside?: "))

# check if temp is greater than or equal to 0 and less than 30

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today.")
    print("Stay inside.")