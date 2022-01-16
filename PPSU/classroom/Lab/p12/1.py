class addressbook:
    def __init__(self,contact_no,name):
        self.contact_no=contact_no
        self.name=name

    def Accressor(self):
        return [self.contact_no,self.name]

    def Setter(self,contact_no,name):
        self.contact_no=contact_no
        self.name=name

a1=addressbook(123456,"ayush")
print(a1.Accressor())
a1.Setter(918765,"vinay")
print(a1.Accressor())