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
    with open("input.txt") as file:
        for n in file:
            print(binaryToDecimal(list(n.rstrip())))

main()
