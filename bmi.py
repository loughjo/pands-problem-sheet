# Program to calculate somebody's Body Mass index (BMI)
# Author: John Loughnane

# https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python
# https://www.youtube.com/watch?v=PpuiO6WJxic = bmi formula

# Use input function to accept inputs from user for weight and height
# Since input function holds a string we need to convert it to an integer by using int
# Once the User enters their weight in kgs we convert the STRING to an INT and assign it to variable WEIGHT.
# We do the same when the user enters their height in cms convert the STRING to an INT and assign the value to variable height.
weight = int(input('Enter your weight in kilograms : '))
height = int(input('Enter your height in centimetres : '))

# Calculate the BMI from the height and weight that was entered
# Use the round function to round the bmi to 2 decimal places => round(number, digits) => number to be rounded and digits is number of decimals.
# formula => weight(kg)/ height (m2) - divide height by 100 to convert to metres.
bmi = round(weight/((height/100)**2),2)

# Print out the BMI answer that was calculated
# Usng the format method which formats the value assigned to variable bmi which is a FLOAT and formats it to a STRING
# and inserts it into the string placeholder {}
# \u00b2 gives the squared 
print('The BMI is (kg/m\u00b2): {}'.format(bmi))