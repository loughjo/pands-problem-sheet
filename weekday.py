#
# Author John Loughnane

from datetime import datetime


#day = datetime.today()
#print(day)
dayOfWeek = ""

#weekday = datetime.weekday(datetime.today())
weekday = 0
#print(weekday)
listWeek = [[0, "Monday"], [1, "Tuesday"], [2, "Wednesday"], [3, "Thursday"], [4, "Friday"], [5, "Saturday"], [6, "Sunday"], ]
#if weekday == 2:
#    print("Today is Wednesday which is a week day")
#else:
#    print("Good day")

#print(listWeek[2])

for i in listWeek:
    for number in i:
        if number == weekday and number <= 4:
            #print(i[1])
            dayOfWeek = "Yes, unfortunately today is a weekday."
            print(dayOfWeek, )
        elif number == weekday and number >= 5: 
            dayOfWeek = "It is the weekend, yay!"
            print(dayOfWeek)
        #else:
         #   print("There is something wrong with teh program")

#print(dayOfWeek)       
