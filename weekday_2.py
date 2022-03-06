

from datetime import datetime


dayOfWeek = ""
# Variable weekday which is assigned and int (index). With 0 = Monday, 1 = Tuesday, 2 = Wednesday etc...
weekday = datetime.weekday(datetime.today())

# I used this piece of code to test whether my program worked correctly.
# Assign a number between 0 to 6 with each number represent a day of the we week
#weekday = 6

# List which holds int 0 to 6 to represent the days of the week. 
# 0 = Monday, 1 = Tuesday, 2 = Wednesday etc....
listWeek = [0, 1, 2, 3, 4, 5, 6]
#if weekday == 2:
#    print("Today is Wednesday which is a week day")
#else:
#    print("Good day")

#print(listWeek[2])
# We loop through the list and first check if i equals weekday AND if i is less than or equal to 4
# if that is TRUE we know that the day is a weekday. If not we then check if weekday is greater than
# or equal to 5 and if that's the case then it is the weekend.

for i in listWeek:
    if i == weekday and i <= 4:
        print("Yes, unfortunately today is a weekday.")
    elif i == weekday and i >= 5: 
        print("It is the weekend, yay!")
        