#Claire Yegian
#9/1/17
#slope.py - calculates slope of a line

x1 = float(input('x1 = '))
x2 = float(input('x2 = '))
y1 = float(input('y1 = '))
y2 = float(input('y2 = '))
slope = float((y1-y2)/(x1-x2))
intersection = float(y1-(slope*x1))
print('The slope is', slope)
print('The equation of the line is Y =', slope, 'X +', intersection)