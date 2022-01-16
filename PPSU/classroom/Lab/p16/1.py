try:
    a=1/0
    print(a)
except (TypeError,ZeroDivisionError):
    print("Not possible to divide by zero...")