def per():
    x, y = input("Fraction: ").split("/")
    percent = int(x) / int(y) * 100
    if int(x) > int(y):
        raise ValueError

    if percent <= 1:
        print("E\n")

    elif percent >= 99:
        print("F\n")

    else:
        print(round(int(x) / int(y) * 100), "%", sep = "")

while True:
    try:
        per()
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break

