# Write a program that asks the user to input any positive integer and then calculates and outputs the collatz sequence
# Author John Loughnane

# Asks the user to enter a positive integer and converts the String input to and integer and assigns it to a variable called number
number = int(input('Please enter a positive integer : '))

# Create an empty string variable called collatzSequence and add the positive integer that was entered 
collatzSequence = " "
collatzSequence += str(number) + " "

# A while loop to keep looping as long as number is not equal to 1. We need to stop whe the current value reaches 1
# if number has a remainder of 0 (even) we need to divide the number by 2 and add it to the string 
#  we assign the output value you to number 
# else teh current number has to be an odd number so we triple the number and add 1 
while number != 1:
    if number % 2 == 0:
        number = number // 2
        collatzSequence += str(number) + " "
    #elif number % 2 == 1:
    else:
        number = (number * 3) + 1
        collatzSequence += str(number) + " "

# We print the complete collatz sequence ouput   
print(collatzSequence)