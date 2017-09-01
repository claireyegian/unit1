#Claire Yegian
#8/31/17
#tipCalculator.py - calculates tips

price = float(input('Price of meal (in dollars): '))
tip = int(input('% to tip: '))
total = price*(tip/100)
print('You should tip', round(total,2))