# convert decimal to binary

def reverseNumber(n):
    reversed = n[::-1]
    return reversed

def binaryToDecimal(n): 
    sum = 0
    num_bits = len(n)
    for p in range(num_bits):
        sum += int(reverseNumber(n)[p]) * 2 **p
    return sum

def main():
    user_input = input("Which number system is your input?\nBase: ")
    conversion = input("Which number system are you converting to?\nBase: ")
    if user_input == "2" and conversion == "10":
        n = list(input("Give me a base 2 number: "))
    print("\nBase 10:", binaryToDecimal(n))

main()
