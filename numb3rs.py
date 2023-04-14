import re
import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if matches:
        a, b, c, d = matches.groups()
        if 0 <= int(a) <= 255 and 0 <= int(b) <= 255 and 0 <= int(c) <= 255 and 0 <= int(d) <= 255:
            return True
    return False



if __name__ == "__main__":
    main()