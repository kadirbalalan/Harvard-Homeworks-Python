import inflect
p = inflect.engine()

list = []

while True:
    try:
        name = input()
        list.append(name)
    except EOFError:
        mylist = p.join((list))
        print("Adieu, adieu, to", mylist)
        break