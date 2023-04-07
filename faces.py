
def convert(txt):
    return txt.replace(":)", "🙂").replace(":(", "🙁")

def main():
    smile = convert(input("Smile for me like this :) If you're sad... you can just frown like this :("))
    print(smile)
main()