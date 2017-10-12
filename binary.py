#Claire Yegian
#10/12/17
#binary.py - converts 8 digit binary to base 10

binary = int(input('Enter an eight-digit binary number: '))

one = (binary%10)
two = ((binary//100)%10)*2
three = ((binary//1000)%10)*4

print(one+two+three)