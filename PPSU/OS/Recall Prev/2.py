s1=input("Enter a 1st number: ")
s2=input("Enter a 2nd number: ")

def swap(s1,s2):
    s1,s2=s2,s1
    print("after swapping:",s1,s2)

swap(s1,s2)