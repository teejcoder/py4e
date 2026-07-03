
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