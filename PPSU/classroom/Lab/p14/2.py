class Student:

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


class Test(Student):

    def __init__(self, java, python, c, html, name, branch):
        super().__init__(name, branch)
        self.java = java
        self.python = python
        self.c = c
        self.html = html

    def value(self, name, branch, java, python, c, html):
        return name, branch, java, python, html


class Marks(Test):
    def __init__(self, name, branch, java, python, c, html):
        super().__init__(java, python, c, html, name, branch)
        self.name = name
        self.branch = branch
        self.java = java
        self.python = python
        self.c = c
        self.html = html

    def display(self, name, branch, java, python, c, html):
        print("--Student Details--")
        print("Name: ", name)
        print("--student marks--")
        print("Java: ", java)
        print("Python: ", python)
        print("C Language: ", c)
        print("HTML: ", html)


name = input("Enter student name: ")
branch = input("Enter branch: ")
print("Enter the marks")
java = float(input("Java: "))
python = float(input("python: "))
c = float(input("c: "))
html = float(input("HTML: "))

obj = Marks(name, branch, java, python, c, html)
obj.value(name, branch, java, python, c, html)
obj.display(name, branch, java, python, c, html)








