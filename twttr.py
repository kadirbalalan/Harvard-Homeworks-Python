vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
word = input("Input: ")
x = ""
for i in word:
    if i not in vowels:
        print(i, end = "")
