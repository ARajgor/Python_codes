class name:
    def __init__(self):
        self.m = 0

    def name_inp(self):
        self.m = str(input("Enter Your name: "))

    def name_out(self):
        print("Your name: ", self.m)


n1 = name()
n1.name_inp()
n1.name_out()