class A:
    @staticmethod
    def add(a,b):
        print("sum: ",a+b)
class B:
    @staticmethod
    def minus(c,d):
        print("Minus: ",c-d)

class C(A,B):
    def __init__(self,a,b):
        self.add(a,b)
        self.minus(a, b)

c=C(3,4)