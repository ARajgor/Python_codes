class Complex:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __str__(self):
        return self.a,self.b

ob1=Complex(3,4)
ob2=Complex(2,3)
ob3=ob1-ob2
ob4=ob1+ob2
print(ob3,ob4)
