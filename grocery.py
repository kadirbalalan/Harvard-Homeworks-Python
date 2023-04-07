fruits = []
while True:
    try:
        fruit = input("").upper()
        fruits.append(fruit)
        cou = fruits.count(fruit)
    except EOFError:
        for fruit in sorted(set(fruits)):
            x = fruits.count(fruit)
            print(f"{x}", fruit)
        break
    except KeyError:
        break