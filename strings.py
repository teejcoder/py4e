string = 'well, well, well. Okay, okay okay!'

for i in string:
    if i == 'e' or i == 'a':
        string = string.replace(i, 'x')
print('done >', string)

# zero-indexed strings.
fruit = 'banana'
print(fruit[1], 'a')

#length of string using len()
lstring = len(string)
print(lstring)

# return 2nd last letter of string
print(string[-2])

# string traversal with loops
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index += 1

# Exercise 1: Write a while loop that starts at the last character in the string 
# and works its way backwards to the first character in the string, 
# printing each letter on a separate line, except backwards.
# ind = len(fruit) # 6
# while ind > 0:
#     letter = fruit[ind - 1]
#     print(letter)
#     ind -= 1

# for i in reversed(banana):
#     print(i)

s = 'monty python'
print(s[0:5], 'monty')
print(s[6:], 'python')

# Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# - fruit[:] will return 'banana'
# print(fruit[:])

# strings are immutable once defined.
greeting = 'hello world'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

# LOOPING & COUNTING
word = greeting
count = 0
for letter in word:
    if letter == 'o':
        count += 1
print('count', count)

# Exercise 3: Encapsulate this code in a function named count, 
# and generalize it so that it accepts the string and the letter as arguments.

def count(word: str, letter: str) -> int:
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count
print('COUNT', count('mooloolaba', 'o')) # 4

# the in operator
print('f' in 'forgetful') # true
print('f' in 'what') # false

# string comparison
word = 'apple'
iword = 'orange'

if iword < word:
    print('your word ' + iword + ' comes before apple')
elif iword > word:
    print('your word ' + iword + ' comes after apple')
else:
    print('your word ' + iword + ' is apple')

# STRING METHODS
print(dir(word))

word = 'banana'
print(word.find('na'), 2)
print(word.find('a', 4), 5)
print(word.find('b'), 0)

# string method method
def startswithfunc(str: str, args: any) -> bool:
    return str.startswith(args)

print(startswithfunc('banana', 'ban'))

whitespacestr = "              what.  "
print(whitespacestr)
print(whitespacestr.strip())



# Exercise 4: There is a string method called count that is similar to the function in the previous exercise. 
# Read the documentation of this method at: https://docs.python.org/library/stdtypes.html#string-methods
# Write an invocation that counts the number of times the letter a occurs in “banana”.

def countinvocation(word: str, args: str) -> str:
    return word.count(args)

print(countinvocation('banana', 'b'), 1)
print(countinvocation('banana', 'a'), 3)
print(countinvocation('banana', 'n'), 2)


# PARSING STRINGS
emails = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

atpos = emails.find('@')
print(atpos)
strpos = emails.find(' ',atpos)
print(strpos)
host = emails[atpos:strpos]
print(host)

# FORMATTED STRING LITERALS

camels = 42
years = 7
print(f'i am {years} and i have {camels} camels')


# Exercise 5: Slicing strings
# Take the following Python code that stores a string:
# Use find and string slicing to extract the portion of the string after the colon character 
# and then use the float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'

aftcol = str.find(' ')
print('aftcol>', aftcol)
data = str[19:]
print(data)
host = float(data)
print(host)
print(type(host), 'float')

# Exercise 6: String methods