#Claire Yegian
#8/31/17
#nameAge.py - characters in a name and age next year

name = input('Enter your first and last name: ')
name1, name2 = name.split()
print('Your first name has', len(name1), 'letters, and your last name has', len(name2), 'letters.')
age = int(input('Enter your age: '))
print('Next year you will be', age+1, 'years old')
