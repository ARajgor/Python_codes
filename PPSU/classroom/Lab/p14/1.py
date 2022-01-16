class addition():
    def add(self,a,b,c=None,d=None):
        if c!=None and d!=None:
            return a+b+c+d
        elif c!= None:
            return a+b+c
        else:
            return a+b

a1=addition()
print(a1.add(1,2,3,4))
print(a1.add(1,2,3))
print(a1.add(1,2))