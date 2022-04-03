# A program that ouputs whether or not today is a weekday
# Author : John Loughnane

# To find the current date and time we need to import the datetime module datetime
from datetime import datetime


# Use the datetime.today() module to display the current time in the format '2022-03-20 21:39:06.496691'
# assign this value to variable weekday which will be of type class 'datetime.datetime'
weekday = datetime.today()

# After trying a couple of different ways to find the day of the week I found the isoweekday() function.
# This function returns an integer value which corresponds to the day of the week, with the value 1 given to Monday 
# When we use 'weekday.isoweekday()' it will assign an integer ranging from 1 to 7.
# We will use the range function which starts at 1 and stops at 6 and the range function does not include teh stop value.
# IF the the integer returned from weekday.isoweekday() is RANGE 1, 6 (6 is not included) well it has to be a weekday else it's weekend.

if weekday.isoweekday() in range(1, 6):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")