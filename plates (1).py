letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2:
        return False
    if len(s) > 6:
        return False
    if s[0] not in letters or s[1] not in letters:
        return False
    for i in s:
        if i not in letters and i not in numbers:
            return False
    i = 0
    while i < len(s):
        if s[i] in numbers:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for i in range(len(s)-1):
        if s[i] in numbers:
            if s[i+1] in letters:
                return False
            i += 1







    return True

main()