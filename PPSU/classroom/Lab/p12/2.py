class bank_account:
    def __init__(self,acc_no):
        self.acc_no=acc_no
        self.bal=1000

    def getter(self):
        return self.bal

    def setter(self,acc_no,bal):
        self.bal=bal
        self.acc_no=acc_no

    def withdraw(self,w):
        self.bal=self.bal-w

    def deposit(self,d):
        self.bal=self.bal+d

    def search(self,a):
        account=[1,2,3,4,5]
        if a in account:
            print(f"Welcome.. Account number {a}")
        else:
            print("Account number invalid")

a=int(input("Enter bank account number: "))
b1=bank_account(a)
b1.search(a)
print("Your balance: ",b1.getter())
i=input("for withdraw enter 1 and for deposit enter 2: ")
if i=='1':
    w=int(input("Enter Amount: "))
    b1.withdraw(w)
    print("Your balance: ",b1.getter())
else:
    d=int(input("Enter Amount: "))
    b1.deposit(d)
    print("Your balance: ",b1.getter())
