data = input("Enter data: ")
print("---- Vertical Redundancy check -----")
after = ' '.join(format(ord(x), 'b') for x in data)
print("Binary Data: ",after)
t = []
for i in after.split():
    a = i.count("1")
    if a % 2 != 0:
        i = i + "1"
        t.append(i)
        print("Parity bit is 1: ",i)
    else:
        i = i + "0"
        t.append(i)
        print("Parity bit is 0: ",i)

print("final: ", " ".join(t))