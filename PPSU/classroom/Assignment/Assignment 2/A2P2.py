string=input("Enter a string: ")
change=input("which character you want to replace: ")
count=0
loop=0
for i in string:
    if i==change:
        count=count+1
    if count==2:
        index=loop
        right_string=string[index:]
        left_string=string[:index]
        string=right_string.replace(change,'$')
        print(left_string+string)
        break
    loop=loop+1