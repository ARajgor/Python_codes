#n=int(input('enter the number of process:'))
n=5
p=[1,2,3,4,5]
all=[10,200,302,211,2]
max=[753,322,902,422,533]
need=[]
f=[]
for i in range(n):
    #print('process:',i)
    #p.append(i)
    #x=int(input('enter allocation as A B C:'))
    #all.append(x)
    #y=int(input('enter max:'))
    #max.append(y)
    need.append(max[i]-all[i])
    f.append(0)
#work=int(input("enter available:"))
work = 332
x=0
a=[]
s=[]
for j in range(n):
    if x<n:
        for k in range(n):
            if need[k]<=work and f[k]==0:
                work+=all[k]
                s.append(p[k])
                x+=1
                f[k]+=1
print(s)