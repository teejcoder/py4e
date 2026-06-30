# Booolean

print(5 == 5, True)
print(5 == 6, False)

# chained conditional w. try / except
x = input('Enter a number or watevr: \n')
try:
    y = int(x)
    if y <= 10:
        print('small')
    elif y <= 20:
        print('medium')
    else:
        print('large')
except:
    print('enter a number next time lol')
    input('enter another num')

#nested conditionals
a = input('enter a num: \n')
b = input('enter another num: \n')
try :
    a = int(a)
    b = int(b)
    if a == b:
        print('a equals b')
    elif a < b:
        print('a is less than b')
    else: 
        print('a is more than b!!! MASSIVE!')
except: 
    print('enter a number lol')


# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# enter hours
# enter rate
# if hours > 40 pay rate * 1.5

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours = input('Enter hours: \n')
rate = input('enter rate: \n')

try:
    fh = float(hours)
    fr = float(rate)
except:
    print('ERROR: please enter a numeric input.')
    quit()

if fh > 40:
    print('overtime!')
    reg = fh * fr
    otr = (fh - 40) * (fr *  0.5)
    print(reg, otr)
    pay = reg + otr
else:
    print('regular!')
    pay = fh * fr
print("total pay:",pay)

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:

score = input('enter a number between 1 - 100: \n')
try:
    score = int(score)
except:
    print('ERROR: please enter a numeric input.')
    quit()
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
elif score < 60:
    print('F')