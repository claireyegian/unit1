#Claire Yegian
#9/6/17
#change.py - finds change in given amount of money

money = int(input('Input a number of cents: '))
quarters = (money//25)
dimes = ((money-(quarters*25))//10)
nickels = ((money-(quarters*25+dimes*10))//5)
pennies = ((money-(quarters*25+dimes*10+nickels*5))//1)
print('You have', quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels, and', pennies, 'pennies.')
