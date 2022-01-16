class Person:

    def __init__(self, name, age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,__empcode):
        self.__empcode=__empcode
        Person.__init__(self,name,age)

    def getall(self):
        return self.name,self.age,self.__empcode

    def setall(self,name,age,__empcode):
        self.name=name
        self.age=age
        self.__empcode=__empcode
        print("Employeee Details ..\n")
        print('Employee Code : ',self.__empcode)
        print('Employee Name : ',self.name)
        print('Age : ',self.age)


empcode=input('Enter the Employee code : ')
name=input('Enter the employee name : ')
age=int(input('Enter the age : '))
emp=Employee(name,age,empcode)
emp.getall()
emp.setall(name,age,empcode)