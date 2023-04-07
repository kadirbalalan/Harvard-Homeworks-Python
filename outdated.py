months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    if "/" in date:
        if not all(c.isnumeric() or c == "/" or c == " " for c in date):
            continue
        resultdate = date.split("/")
        if int(resultdate[0]) > 12:
            continue
        if int(resultdate[1]) > 31:
            continue
        print(f"{int(resultdate[2])}-{int(resultdate[0]):02d}-{int(resultdate[1]):02d}")
        break
    if "," in date:
        try:
            if "/" in date:
                continue
            date = date.replace(",", "")
            resultdate2 = date.split(" ")
            month_index = months.index(resultdate2[0]) + 1
            if int(resultdate2[1]) > 31:
                continue
            print(f"{int(resultdate2[2])}-{month_index:02d}-{int(resultdate2[1]):02d}")
            break
        except ValueError:
            continue
    else:
        continue
