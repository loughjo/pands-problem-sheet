# A program that ouputs whether or not today is a weekday
# Author : John Loughnane

# To find the current date and time we need to import the datetime module datetime
from datetime import datetime

print(datetime.today())
# Variable weekday which is assigned and int (index). With 0 = Monday, 1 = Tuesday, 2 = Wednesday etc...
weekday = datetime.weekday(datetime.today())

# An if/else statement which checks the integer variable weekday
# If the value is less than or equal to 4 it is a weekday otherwise it must be 6 or 7 which is a Weekend.
 
if weekday <= 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

