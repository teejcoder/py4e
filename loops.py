
for i in [5,4,3,2,1]:
    print(i)
print('BLASTTOFFFF!!!!')


#assign largest_num to variable
largest_num = 0
print("BEFORE", largest_num)
for i in [1,2343,567,6,5432,12,345,6787,654,56,78,7654,3,456,78,97,654,3,45,67890,8,7654,3,456,789,87,654,5]:
    if i > largest_num: #compare list[0] to largest_num
        largest_num = i #if list[0] > largest_num replace largest num
    print(largest_num)
print('AFTER', largest_num)
#return largest num


# THE WHILE STATEMENT

n = 5 #iteration variable
while n > 0: # logical expression
    print(n)
    n = n - 1
print("blastoff!")

#INFINITE LOOPS
#ni = 0 # iteravtion variable
#while n < 5: # logical expression
#    print('infinite loop')

# no iteration variable on this loop
#while True: # logical constant - True
#    print('also an infinite loop')

while True:
    uval = input('> enter a word, type done to exit \n')
    if uval == 'done':
        break
    print(uval)
print('done!')


# finishing iterations with Continue

while True:
    uval = input('> ')
    if uval[0] == '#':
        continue
    if uval == 'done':
        break
    print(uval)
print('DONE!')

# definite loops using FOR

friends = ['jilly', 'billy', 'milly'] # list of strings assigned to variable 'friends'
for i in friends: # iteration variable i iterating over friends list
    print('Hello friend with name', i)
print('CEASE GREETING')

# LOOP PATTERNS

# counting & summing loops

#count the number of items in this list with a for loop
count = 0
for i in [1,2,3,4,5,6]:
    count += 1
print('number of items in list', count)

total = 0
for i in [1,2,3,4,5]:
    total += i
print('total', total)

# MAXIMUM & MINIMUM LOOPS
largest = None
print('before:', largest)
for intervar in [2,345,67,65,4,3,45,6,7,654,4,564]:
    if largest is None or intervar > largest:
        largest = intervar
    print('Loop', intervar, largest)
print('LARGEST', largest)

smallest = None
print('BEFORE:', smallest)
for i in [3000,300,45,67,65,43,2,3,45,6,78,7,65,43,45,7,5,43,2,1]:
    if smallest is None or i < smallest:
        smallest = i
    print('LOOP>', i, smallest)
print('SMALLEST:', smallest)

# EXERCISE 1 - Write a program which repeatedly reads integers 
# until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average 
# of the integers. If the user enters anything other than an integer, 
# detect their mistake using try and except and print an error message 
# and skip to the next integers.
# total = 0.0
# count = 0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try: 
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    total = total + fval
    count += 1
print('done!')
print('total:', total, 'count:', count, "avg:", total/count)


# Exercise 2: Write another program that prompts for a 
# list of numbers as above and at the end prints out 
# both the maximum and minimum of the numbers instead of the average.

nums = []
while True:
    sval = input('enter a number: \n')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    nums.append(fval)
print('MAX:', max(nums), 'MIN: ', min(nums))