#Claire Yegian
#10/12/17
#binary.py - converts 8 digit binary to base 10

binary = int(input('Enter an eight-digit binary number: '))

one = (binary%10)
two = ((binary//10)%10)*2
three = ((binary//100)%10)*4
four = ((binary//1000)%10)*8
five = ((binary//10000)%10)*16
six = ((binary//100000)%10)*32
seven = ((binary//1000000)%10)*64
eight = ((binary//10000000)%10)*128

print(one+two+three+four+five+six+seven+eight)