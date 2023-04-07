hello = input("Greet!").strip().lower()
if hello.startswith("h") and not hello.startswith("hello"):
    print("$20")
elif hello.startswith("hello"):
    print("$0")
else:
    print("$100")