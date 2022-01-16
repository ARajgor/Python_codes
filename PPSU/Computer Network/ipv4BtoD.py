#IPv4 address convert into binary

text = '192.162.0.1'
print('.'.join(format(int(x), '08b') for x in text.split('.')))
