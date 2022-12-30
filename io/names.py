# names = []

# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)

# for name in sorted(names):
#     print(f"Hello, {name}")
    

# file = open("names.txt", "w") # open returns a file handel
# with open("names.txt", "a") as file:
#   file.write(f"{name}\n")
file = open("names.txt", "w")

for _ in range(3):
    name = input("What's your name? ")
    file.write(f"{name}\n")
file.close()    
