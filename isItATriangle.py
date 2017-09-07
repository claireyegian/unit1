#Claire Yegian
#9/7/17
#isItATriangle.py - find if entered values can be the sides of a triangle

side1 = float(input('Enter the length of the first side: '))
side2 = float(input('Enter the length of the second side: '))
side3 = float(input('Enter the length of the third side: '))
long = float(max(side1,side2,side3))
short = float(min(side1,side2,side3))
mid = float(side1+side2+side3-long-short)
print((mid+short)>long)
