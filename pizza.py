import sys
from tabulate import tabulate
import csv
lst = []
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(f"{sys.argv[1]}") as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append({"pizza": row[0], "small": row[1], "large": row[2]})
    for i in lst:
        print(tabulate(lst, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
