def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n ** 2
    # return pow(n, 2)
    
main()
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = (x / y)

# print(f"{z:.2f}")
# print(f"{z:,}")