# Program to calculate somebody's Body Mass index (BMI)
# Author: John Loughnane

# Use input function to accept inputs from user for weight and height
weight = input('Enter your weight in kilograms : ')
height = input('Enter your height in centimetres : ')

# Calculate the BMI from the height and weight that was entered
bmi = (int(weight))/(int(height)/100)
bmi = bmi / (int(height)/100)

print('The BMI is (kg/m*2): ' + str(bmi))