#Claire Yegian
#9/11/17
#quiz1.py - prints name, sum and product of two numbers, lucky number

from random import randint

name = input('Enter your name: ')
print(name)
num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))
print('The sum is', num1+num2)
print('The product is', num1*num2)
print('Your lucky number is', randint(9,9))
