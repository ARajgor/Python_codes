hours=int(input("enter week hours :"))
rate=int(input("enter hour rate :"))

if hours>40:
    extra=hours-40
    pay=(1.5*extra*rate)+(rate*hours)
    print("over time pay:",1.5*extra*rate)
    print("total pay:",pay)

else:
    print("total pay: ",hours*rate)