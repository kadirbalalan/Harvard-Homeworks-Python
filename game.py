import random
import sys


while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            continue
    except ValueError:
        continue
    p = random.randint(1, n)
    while True:
        try:
            g = int(input("Guess: "))
        except ValueError:
            continue
        if g == p:
            print("Just right!")
            sys.exit()
        if g < p:
            print("Too small!")
        if g > p:
            print("Too large!")