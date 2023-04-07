i = 50
while i > 0:
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        print("Amount Due:", int(i) - int(insert))
        i = i - int(insert)
    else:
        print("Amount Due:", int(i))
i = abs(i)
print("Change Owed:", int(i))