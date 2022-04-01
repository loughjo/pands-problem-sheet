# A program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author : John Loughnane

# 
number = float(input("Please enter a positive number: "))

# Two variables defined, variable count is use in the IF statement when count equals 0 
# we will run the IF statement or ELSE we will do something different. 
# The approximation variable is assigned 
count = 0
approximation = 0

# While the variable number which is entered is NOT EQUAL to approximation * approximation continue with the IF/ELSE statment
# The approxiamation variable is our estimation of the SQUARE ROOT so if this result is EQUAL to number we stop.
# We round the approximation * approximation to 1 decimal place. 
while number != (round(approximation*approximation,1)) :
    if count == 0:
        approximation = (number + (number/number))/2
        count +=1
        #print(approximation)
    else:
        approximation = (approximation + (number/approximation))/2
        #count += 1
        #print(approximation)

# We round float number assigned to the approximation variable to one decimal place as this is required for the answer.
# Then we print the approximation calculated 
approximation = round(approximation,1)
print('The square root of {} is approx. {}.'.format(number, approximation))