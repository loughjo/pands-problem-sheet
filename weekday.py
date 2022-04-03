# A program that ouputs whether or not today is a weekday
# Author : John Loughnane

# https://www.w3schools.com/python/python_datetime.asp
# https://stackoverflow.com/questions/1907196/how-do-i-check-if-its-monday-to-friday-and-the-time-is-between-10-am-to-3-pm
# To find the current date and time we need to import the datetime module datetime
from datetime import datetime


# Use the datetime.today() module to display the current time in the format '2022-03-20 21:39:06.496691'
# assign this value to variable weekday
weekday = datetime.today()
print(type(weekday))

# the value is assigned to the variable 'weekday' where weekday.isoweekday() displays the day of teh week as an integer
if weekday.isoweekday() in range(1, 6):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")