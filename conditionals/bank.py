
greeting = input("Greeting: ").lower()
h = "h"

if greeting == "hello":
    print("$0")
elif greeting != "hello":
    if greeting.rfind(h) == 0:
        print("$20")
    else:
        print("$100")