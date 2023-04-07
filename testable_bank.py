
def main():
    hello = input("Greet!").strip().lower()
    print(f"${value(hello)}")


def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("h") and not greeting.startswith("hello"):
        return 20
    elif greeting.startswith("hello"):
        return 0
    else:
        return 100

if __name__ == "__main__":
    main()