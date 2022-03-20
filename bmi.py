# Program to calculate somebody's Body Mass index (BMI)
# Author: John Loughnane

# https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python
# https://www.youtube.com/watch?v=PpuiO6WJxic = bmi formula

# Use input function to accept inputs from user for weight and height
# Since input function holds a string we need to convert height and weight to an integer so we can calaculate the BMI.
weight = int(input('Enter your weight in kilograms : '))
height = int(input('Enter your height in centimetres : '))

# Calculate the BMI from the height and weight that was entered
# Use the round function to round the bmi to 2 decimal places
# formula => weight(kg)/ height (m2) - divide height by 100 to covert to metres.
bmi = round(weight/((height/100)**2),2)

# Print out the BMI a nswer that was calculated
print('The BMI is (kg/m*2): ' + str(bmi))