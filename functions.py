# # FUNCTION CALLS
# print(type(10)) # function = type(), argument = 10, return value = int
# print(type(1.2)) # function = type(), argument = 1.2, return value = float
# print(type('hello, world')) # function = type, argument = 'hello, world', return value = str


# # BUILT-IN FUNCTIONS
# print(max('hello, world!')) # function = max, argument = 'hello, world!', return value = w
# print(min('hello world!')) # function = min, argument = 'hello, world!, return value = ' '
# print(len('hello, world')) # function = len, argument = 'hello, world', return value = 12


# # TYPE CONVERSION FUNCTIONS
# print(int(3.2)) # 3
# print(float(32)) # 32.0
# xx = 32 
# xx = str(xx)
# print(xx, type(xx)) # 32 <class 'str'>


# # MATH FUNCTIONS
import math

# print(math)

# signal_power = 10
# noise_power = 5
# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)
# print(decibels) # 3.010299956639812

# degrees = 45
# radians = degrees / 360.0 * 2 * math.pi
# print(math.sin(radians)) # 0.7071067811865475

# print(math.sqrt(2) / 2.0)


# # RANDOM NUMBERS - returns a random float between 0.0 - 1.0, including 0.0 but not 1.0
# import random

# for i in range(10):
#     x = random.random()
#     print(x)


# # randint() - returns a random int between low and high parameters.
# na = random.randint(1,5)
# nb = random.randint(5,10)
# print(na, nb)

# # choice() - chooses an element from a sequence at random
# t = [1,2,3,4,5,6,7,8,9,10]
# print(random.choice(t))



# # ADDING NEW FUNCTIONS
# def print_lyrics() -> str:
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night, and I work all day.")

# print(print_lyrics, 'function print_lyrics')
# print(type(print_lyrics), "<Class 'function'>")

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# repeat_lyrics()


# # DEFINITIONS AND USES

# PARAMETERS AND ARGUMENTS
# user defined function that takes an argument and prints it twice.
def print_twice(x: str) -> str:
    print(x)
    print(x)

pam = 'pee pee halbert'

print_twice(pam)


# FRUITFUL FUNCTIONS AND VOID FUNCTIONS
math.sqrt(5)

# functions using return
def add_two(a:int, b:int)->int:
    return a + b

na = add_two(10,10)
nb = add_two(100,100)
nc = add_two(1,1)
print(na,nb,nc)

def sum_arr(arr) -> int:
    return sum(arr)

ni = sum_arr([10,10])
nj = sum_arr([100,100])
nk = sum_arr([1,1])

print(ni, nj, nk)


# # EXERCISE 1 - run the random() program on your machine to see what numbers you get. 
# # Run the program more than once and see what numbers are returned

# 0.08493067404825416
# 0.3375126511419494
# 0.7550321649813468
# 0.5147105533252399
# 0.2872333090327045
# 0.681754278593091
# 0.5738689019488872
# 0.8173471869264921
# 0.3824838560855238
# 0.3772188108244555

# 0.05717687482538536
# 0.43624071155741173
# 0.9816060426134022
# 0.05498667381838418
# 0.7012370751395965
# 0.007681961853421404
# 0.8642537924470269
# 0.10971106273161435
# 0.2393436104195128
# 0.33870877720245063


# # Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. 
# # Run the program and see what error message you get.

# # repeat_lyrics()

# # def print_lyrics():
# #     print("I'm a lumberjack, and I'm okay.")
# #     print('I sleep all night and I work all day.')

# # def repeat_lyrics():
# #     print_lyrics()
# #     print_lyrics()
    
# #Traceback (most recent call last):
# #  File "/Users/teej/Desktop/py4e/functions.py", line 105, in <module>
# #    repeat_lyrics()
# #NameError: name 'repeat_lyrics' is not defined


# # Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. 
# # What happens when you run this program?

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
    
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# repeat_lyrics()


# Exercise 4: What is the purpose of the “def” keyword in Python?
# a) It is slang that means “the following code is really cool”
# b) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true <- this is the answer
# e) None of the above

# Exercise 5: What will the following Python program print out?
# def fred():
#    print("Zap")

# def jane():
#    print("ABC")

# jane()
# fred()
# jane()

# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) ABC Zap ABC <- this is the answer
# e) Zap Zap Zap

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

try:
    hours = float(input('Enter hours:\n'))
    rate = float(input('Enter rate:\n'))
except:
    print('please enter a numerical input')
    quit()

def computepay(hours: float, rate: float)-> float:
    if hours > 40:
        base = hours * rate
        oth = hours - 40
        otr = rate * 0.5
        otp = oth * otr
        return base + otp
    return hours * rate

print(computepay(hours, rate), 475.0)
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade 
# that takes a score as its parameter and returns a grade as a string.
try: 
    score = float(input('Enter your score between 0.0 - 1.0: \n'))
except:
    print('please enter a number between 0.0 and 1.0')
    quit()
        
def computegrade(score:float)-> str:
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else: 
        return "F"

print(computegrade(score))
