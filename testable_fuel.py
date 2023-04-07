def main():
    n = input("Fraction: ")
    percentage = convert(n)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            percentage = round(int(x) / int(y) * 100)
            if not x.isnumeric() or not y.isnumeric():
                raise ValueError
            elif int(x) > int(y):
                raise ValueError
            elif int(y) == 0:
                raise ZeroDivisionError
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E\n"
    elif percentage >= 99:
        return "F\n"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
