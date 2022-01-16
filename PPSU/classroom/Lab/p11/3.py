class calc:
    def __init__(self,a,o,b):
        self.a=a
        self.o=o
        self.b=b
    def Operations(self):
        if self.o == '+':
            print(self.a," + ",self.b,' = ',self.a+self.b)
        elif self.o == '-':
            print(self.a," - ",self.b,' = ',self.a-self.b)
        elif self.o == '*':
            print(self.a," * ",self.b,' = ',self.a*self.b)
        elif self.o == '/':
            print(self.a," / ",self.b,' = ',self.a/self.b)
        elif self.o == '%':
            print(self.a," % ",self.b,' = ',self.a%self.b)
        elif self.o == '^':
            print(self.a," ^ ",self.b,' = ',self.a**self.b)
        else:
            print("Invalid choice!!")
        return 0

c1=calc(10,'+',20)
c1.Operations()
c1=calc(100,'-',20)
c1.Operations()
c1=calc(10,'*',20)
c1.Operations()
c1=calc(10,'/',20)
c1.Operations()
c1=calc(10,'%',20)
c1.Operations()
c1=calc(10,'^',2)
c1.Operations()