def main():
    fuel = get_fuel("Fraction: ")

    if fuel >= 99 and fuel <= 100:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")

def get_fuel(fraction):

    while True:
        try:
            str = input(fraction)
            split = str.split("/")
            x = int(split[0])
            y = int(split[1])

            if x > y:
                raise Exception("improper fraction")

            percentage = round(x/y*100)
            return percentage

        except Exception as e:
            print(e)
            pass
        except ValueError:
            print("value error")
            pass
        except ZeroDivisionError:
            print("cannot divide by 0")
            pass


main()
