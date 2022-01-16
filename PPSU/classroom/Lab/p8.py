#1.  Write a code to create a dictionary
dict = {
    'Thriller':1982,
    'Back in Black':1980,
    'The Dark Side of The Moon':1973,
    'The Bodyguard':1992,
    'Bat Out Of Hell':1977,
    'Their Greatest...':1976,
    'Saturday Night Fever':1977,
    'Rumours':1977
}
#print(dict)



#2. Write code to perform following operations
#a
# print(dict.keys())
#
# #b
# print(dict.values())
#
# #c
# dict.update({'name' : 'Ayush rajgor'})
# print(dict)
#
# #d
# dict.pop('Thriller')
# print(dict)
# #e
#
# print('name' in dict)

# # 3. Write a program to create a dictionary with cricket players name and
# # scores in a match. Retrieve runs of any player when player’s name is given.
new_dict = {
    'sachin' : 119,
    'sahevag' : 100,
    'kohli' : 99,
    'dhoni' : 190
}

player_name = 'dhoni'

#print(new_dict[player_name])

# 4. Write a program to sort the elements of a dictionary based on a key or
# value.

print(sorted(new_dict.items()))


