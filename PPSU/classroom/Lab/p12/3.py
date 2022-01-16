class student:
    def __init__(self,roll,marks,name):
        self.roll=roll
        self.marks=marks
        self.name=name

    def Accessor(self):
        return self.roll,self.marks

    def Setter(self,roll,marks,name):
        self.roll=roll
        self.marks=marks
        self.name=name

a1=student(1,78,'ayush')
print("Old: ",a1.Accessor())
a1.Setter(2,97,'vinay')
print("After update: ",a1.Accessor())