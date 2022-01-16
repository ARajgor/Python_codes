a='ffbbf fvef five point dhgfhd efbeu'
li=list(a.split(" "))
n=li.index("point")
li[n]='and'
li.append('paisa')
st = ' '.join([str(x) for x in li])
print(st)