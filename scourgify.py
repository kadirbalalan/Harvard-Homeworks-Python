import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
if not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

with open(f"{sys.argv[1]}", newline="") as file:
    reader = csv.DictReader(file)
    with open(sys.argv[2], "w") as newfile:
        writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})