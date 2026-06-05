x = 4
x = x - 2
print(type(x))
print(x)
print(1,000,000)

msg = 'And now for something completely different!'
n = 3.14159
print(msg)


def loop_to_10():
    n = 0
    while n < 10:
        n += 1
        print(n)
        if n == 10:
            print('DONE~!')


loop_to_10()


# Operators and operands
# Operators are special symbols that represent computations like addition and multiplication. The values the operator is applied to are called operands.

print(10**5)
minute = 59
print(minute//60)


# Expressions
# An expression is a comination of values, variables and operators. Single values are considered expressions, so are variables. The following qare all legal expressions
y = 5
y = y + 1
print(y)

# Order of operations - PEMDAS - Parenthesis, Exponentiation, Multiplication, Division, Addition, Subtraction.
pem_das = (10 * 40) ** (1/1) + 21 - .31
print(pem_das) # 420.69

# modulo
print(7%3) # 1


first = "10"
second = "20"
print(first+second) #1020

# INPUT 
# inp = input("Write silly input/s: \n")
# print(inp)

# prompt = "WHat is the airspeed velocity of an unladen swallow?"
# speed = input(prompt)
# int(speed)

# print(speed)


def pay_rate_calc(rate: int, hours: int):
    return rate * hours

print(pay_rate_calc(38, 40))

pizza = [1,2,3,4,5,6,7,8,9,10]

for n in pizza:
    print(n)


#Exercises

#Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
get_user_name = input("Enter your name: \n")
print("Hi,", get_user_name)

#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
def pay_rate_calc():
    rate = input("Enter your rate\n")
    hours = input("How many hours did you work this week?\n")
    print("This is your pay this cycle:", int(rate) * int(hours))
pay_rate_calc()


# Exercise 4: Assume that we execute the following assignment statements: 
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).

width = 17
height = 12.0

# width//2
# 8
# width/2.0
# 8.5
# height/3
# 4.0
# 1+2*5
# 11

# Exercise 5: Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.

def celsius_to_farenheit():
    celsius = int(input("Enter the temperature in Celsius \n"))

    farenheit = (9 * celsius/5) + 32
    print("Farenheit temp:", farenheit)

celsius_to_farenheit()