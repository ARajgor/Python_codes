class Student:
    def __init__(self):
        self.m = 0
        self.c = 0
        self.p = 0

    def input(self):
        self.m = int(input("Maths mark: "))
        self.c = int(input("Chemistry mark: "))
        self.p = int(input("Physics mark: "))

    def output(self):
        print("Your Maths mark: ", self.m)
        print("Your Chemistry mark: ", self.c)
        print("Your Physics mark: ", self.p)


s1 = Student()
s1.input()
s1.output()