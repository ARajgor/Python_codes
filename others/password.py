import random

C=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
S=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
N=['1','2','3','4','5','6','7','8','9','0']
sy=['#','@','_']

small=[]
capital=[]
num=[]
symb=[]

for i in range(0,2):
    small.append(S[random.randint(0,25)])
for i in range(0,3):
    capital.append(C[random.randint(0,25)])
for i in range(0,2):
    num.append(N[random.randint(0,9)])
for i in range(0,2):
    symb.append(sy[random.randint(0,2)])

pas=[small,num,symb,capital]
def convert(s):
    string=""
    for i in s:
        string+=i
    return string

pre=[]
for i in pas:
    pre.append(convert(i))
password=convert(pre)
print(password)