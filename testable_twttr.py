vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(n):
    longword = ""
    for i in n:
        if i not in vowels:
            longword += i
    return longword


if __name__ == "__main__":
    main()