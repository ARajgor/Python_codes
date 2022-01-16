file = open("file1.txt", 'w')

file.write("This is Delhi \n")
file.write("This is Paris \n")
file.write("This is London\n")
file.close()

num_line = 0
num_word = 0
num_char = 0
with open("file1.txt", 'r') as f:
    for line in f:
        num_line += 1
        a=line.rstrip()
        word=a.split()
        num_word = num_word + len(word)
        for i in word:
            num_char = num_char + len(i)

print("Numbers of line: ",num_line)
print("Numbers of word: ",num_word)
print("Numbers of char: ",num_char)