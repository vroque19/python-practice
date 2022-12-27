def main():
    name = input("What's your name? ")
    # hello()
    hello(name.title().strip())
# Ask user for their name
# name = input("What's you name? ").strip().title()

# Remove whitespace from left and right of str
# A method is a function built in
# name = name.strip().title()

# Split user's name into first name and last
# first, last = name.split(" ")


# Say hello to user
# print(f"Hello, {first}")

def hello(to="world!"):
    print("hello,", to)

main()
