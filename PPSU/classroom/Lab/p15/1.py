file = open("file1.txt" , "w") # create a file
file.write(str(input("Enter your stuff hear : ")))
file.close()
file = open('file1.txt' , 'r')
print('In file : ' , file.read())
file.close()