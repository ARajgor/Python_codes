day=int(input("Enter days: "))

def convert(day):
    if day<30:
        print(f"month: 0 and days: {day}")
    elif day>=30:
        m=int(day/30)
        d=day-(30*m)
        print(f"month: {m} and days: {d}")

d=convert(day)
