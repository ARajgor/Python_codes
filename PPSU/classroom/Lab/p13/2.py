class Person:
    def __init__(self,name,age):
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
        print("===========================================\n")
        print("Employeee Details ..\n")
        print('Employee Code : ',self.__empcode)
        print('Employee Name : ',self.name)
        print('Age : ',self.age)

class Manager(Employee):

    def __init__(self,name,age,empcode,dept):
        self.dept=dept
        Employee.__init__(self,name,age,empcode)
    def getdata(self):
        Employee.getall(self)
        return self.dept
    def setdata(self,name,age,__empcode,dept):
        Employee.setall(self,name,age,__empcode)
        print("Department : ",self.dept)

empcode=input('Enter the Employee code : ')
name=input('Enter the employee name : ')
age=int(input('Enter the age : '))
dept=input('Department : ')
emp=Manager(name,age,empcode,dept)
emp.getdata()
emp.setdata(name,age,empcode,dept)