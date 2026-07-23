# LIST CONSTRUCTORS

# stuff = list()
# stuff.append('book')
# stuff.append(99)
# print(stuff)
# stuff.append('cookie')
# print(stuff)

# some = [1,9,21,34,45,69]
# print(9 in some, True)
# print(12 in some, False)
# print(69 in some, True)

# friends = ['jack', 'jill', 'bob', 'anne']
# topfriends = friends.sort()
# print(topfriends)

# # LISTS ARE MUTABLE
# cheeses = ['gouda', 'camembert', 'roquefort', 'edam', 'cheddar']
# print(cheeses[0])
# print(cheeses)
# cheeses[0] = 'tasty'
# print(cheeses)

# print('gouda' in cheeses)
# print('round' in cheeses)

# # TRAVERSING A LIST
# for cheese in cheeses:
#     print(cheese)

# numbers = [1,2,3,4,5]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print(numbers)

# for i in range(len(cheeses)):
#     cheeses[i] = cheeses[i] * 2
# print(cheeses)

# # LIST OPERATORS
# a = [1,2,3]
# b = [4,5,6]
# print('print a + b: ', a + b)

# zeroth = [0]
# print('zeroth * 4:', zeroth * 4)
# print('a * 4:', a * 4)

# # LIST SLICES
# alphab = ['a', 'b', 'c', 'd', 'e', 'f']
# abc = alphab[:3]
# cdef = alphab[3:]
# print(abc, cdef)
# print(abc + cdef)

# alphab[-3:] = ['x', 'y', 'z']
# print(alphab, ['a,b,c,x,y,z'])

# LIST METHODS
# Most list methods are void; they modify the list and return None. 
# If you accidentally write t = t.sort(), you will be disappointed with the result.

# .append()
# abc = ['a','b','c']
# abc.append('d')
# print(abc)

# # .extend()
# ef = ['e','f']
# abc.extend(ef)
# print('extend():', abc)

# # sort()
# jumbled = ['x','t','e','g','a']
# print('jumbled',jumbled)
# jumbled.sort()

# print('sorted',jumbled)

# DELETING ELEMENTS
# abc = ['a','b','c']

# # pop() returns the value removed BY ITS INDEX
# c = abc.pop()
# a = abc.pop(0)
# print(c, 'c')
# print(a, 'a')

# # del removes the value from the array by its index and returns the array without the value
# t = ['v', 'w', 'x','y','z']
# del t[1]
# print(t, 'vxyz')
# # remove more than one element use the del with slice index
# del t[:1]
# print(t, 'xyz')

# # if you know the element to remove but not its index use remove()
# t = [1,2,3]
# t.remove(2)
# print(t, '1,3')

# LISTS AND FUNCTIONS
# nums = [7,54,32,3,4,567,89,54,32,2,45,7,7,54,3,232,2]

# print('length: ', len(nums))
# print('max num: ', max(nums))
# print('min num: ', min(nums))
# print('sum of nums: ', sum(nums))
# print('average: ', sum(nums)/len(nums))

# # create an empty list -> append each entered value and then compute the average.
# numlist = list()
# while True:
#     inp = input('enter a number, or type done when finished: ')
#     if inp == 'done':
#         break
#     value = int(inp)
#     numlist.append(value)
# avg = sum(numlist) / len(numlist)
# print('AVG: ',avg)

# LISTS & STRINGS

# list() breaks strings in to individual items
# spam = 'spam'
# x = list(spam)
# print(x, ['s', 'p', 'a', 'm'])

# # split() breaks strings in to words
# words = "they're taking the hobbits to eisengard"
# t = words.split()
# print(t)

# # split by a delimiter
# s = 'spam-spam-spam'
# print(s)
# print(s.split('-'))

# # join() is the inverse of split
# delimiter = ' '
# t = delimiter.join(t)
# print(t)

# PARSING LINES
# we want to open mbox-short and return the days after the word 'From:'
# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     days = words[2]
#     print(days)

# OBJECTS AND VALUES
# a = 'banana'
# b = 'banana'
# print(a is b, True)

# c = [1,2,3]
# d = [1,2,3]
# print(c is d, False)

# ALIASING
# a = [1,2,3]
# b = a
# print(b is a, True)
# b[0] = 17
# print(a)

# LIST ARGUMENTS
# def delete_head(t):
#     del t[0]

# letters = ['a','b','c','d','e']
# delete_head(letters)
# print(letters)

# # distinguishing between modifying and creating new lists
# t1 = [1,2,3]
# t2 = t1.append(4)
# print(t1, [1,2,3,4])
# print(t2, None)

# t3 = t1 + [5]
# print(t1)
# print(t3)
# print(t1 is t3, False)

# # Best to create and return a new list rather than modify the original
# def tail(t):
#     return t[1:]

# lett = ['a','b','c','d','e']
# print(tail(lett))


# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# t1 = [1,2,3,4,5]
# t2 = ['a','b','c','d','e']

# def chop(t):
#     t.pop()
#     t.pop(0)

# print(chop(t1), None)
# print(chop(t2), None)

# def middle(t):
#     return t[1:-1]


# print(middle(t1), 3)
# print(middle(t2), 'c')



# Exercise 2: Figure out which line of the above program is still not properly guarded. 
# See if you can construct a text file which causes the program to fail and then 
# modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

# fhand = open('./files/mbox-short.txt')

# for line in fhand:
#     words = line.split()
#     # print('Debug:', words)
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])


# Exercise 3: Rewrite the guardian code in the above example without two if statements. 
# Instead, use a compound logical expression using the or logical operator with a single if statement.
# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) == 0 or words[0] != 'From' : continue
#     print(words[2])

# Exercise 4: Find all unique words in a file
# def unique_words():
#     unique = []
#     fhand = open('./files/romeo.txt')
#     for line in fhand:
#         line = line.split()
#         for word in line:
#             if word in unique: continue
#             unique.append(word)
#     unique.sort()
#     return unique    
    
# print(unique_words())



# Exercise 5: Minimalist Email Client.
# def fromcount():
#     count = 0
#     result = []
#     fhand = open('./files/mbox-short.txt')
#     for line in fhand:
#         line = line.rsplit()
#         if len(line) > 0 and line[0] == 'From':
#             result.append(line)
#             count = count + 1
#         # print('DEBUG: ', line)
#     for i in result:
#         print(i[1])    
#     print(f'There were {count} lines in the file with From as the first word')
# fromcount()

# Rewrite the program that prompts the user for a list of numbers 
# and prints out the maximum and minimum of the numbers at the end 
# when the user enters “done”. Write the program to store the numbers 
# the user enters in a list and use the max() and min() functions to compute the maximum 
# and minimum numbers after the loop completes.

# def minmax():
#     result = []
#     while True:
#         uinput = input('enter a number of type done to exit: ')
        
#         if uinput == 'done':
#             break
        
#         try:
#             result.append(float(uinput))    
#         except ValueError:
#             print('bad input')
#             continue
    
#     print('Min: ', min(result))
#     print('Max: ', max(result))

# minmax()