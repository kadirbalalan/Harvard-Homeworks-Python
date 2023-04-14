import sys
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    try:
        with open(f"{sys.argv[1]}") as file:
            l = file.readlines()
            lenght = len(l)
        for i in l:
            if i.isspace():
                lenght -= 1
            if i.lstrip().startswith("#") or i.startswith("'''"):
                lenght -= 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(lenght)
main()