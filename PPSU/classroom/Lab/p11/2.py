class List:
    def __init__(self):
        self.n = []

    def add(self, a):
        return self.n.append(a)

    def remove(self, b):
        self.n.remove(b)

    def display(self):
        return (self.n)
obj = List()
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice = int(input("Enter choice: "))
    if choice == 1:
        n = int(input("Enter number to append: "))
        obj.add(n)
        print("List: ", obj.display())
    elif choice == 2:
        n = int(input("Enter number to remove: "))
        obj.remove(n)
        print("List: ", obj.display())
    elif choice == 3:
        print("List: ", obj.display())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")