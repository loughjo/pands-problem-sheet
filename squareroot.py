# A program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author : John Loughnane

# Asks the user to enter a positive integer and converts the String input to a FLOAT and assigns it to a variable called number
number = float(input("Please enter a positive number: "))

# Two variables defined, variable count is used in the IF statement. 
# I want to run the IF statement the first time the while loop runs as the formula is different and we increment count by
# When the While loops runs a second time count will NOT EQUAL 0 so the ELSE state will run.
# The approximation variable is assigned 0 and this variable is used to keep track of teh Approximation value.
# This value keeps changing each time the While loop runs until we get as close to the approximation as possible 
count = 0
approximation = 0

# While the variable NUMBER which is entered by the USER is NOT EQUAL to approximation * approximation continue with the IF/ELSE statment
# The approxiamation variable is our estimation of the SQUARE ROOT so if this result is EQUAL to NUMBER value we stop.
# We round the approximation * approximation to 1 decimal place and the WHILE loop keeps looping until NUMBER != (APPROXIMATION*APPROXIMATION).
# The WHILE loop knows now to stop looping and the final Approximation is thn printed out to stdout
while number != (round(approximation*approximation,1)) :
    if count == 0:
        approximation = (number + (number/number))/2
        count +=1
    else:
        approximation = (approximation + (number/approximation))/2

# We round float number assigned to the approximation variable to one decimal place as this is required for the answer.
# Using the format method which formats the value assigned to variable number and approximation and formats them to a STRING
# and inserts it into the relevant string placeholders {}
# Then we print out the approximation calculated. 
approximation = round(approximation,1)
print('The square root of {} is approx. {}.'.format(number, approximation))