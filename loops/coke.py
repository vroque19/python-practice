def main():
    loop()

def loop():
    amount_due = 50

    while amount_due > 0:
        print("Amount due:", amount_due)
        coin = int(input("Insert coin: "))

        if coin in [25, 10, 5]:
            amount_due = amount_due - coin

    print("Change Owed: ", abs(amount_due))

main()