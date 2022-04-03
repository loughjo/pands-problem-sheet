# Write a program that asks the user to input any positive integer and then calculates and outputs the collatz sequence
# Author John Loughnane

# Asks the user to enter a positive integer and converts the String input to an integer and assigns it to a variable called number
number = int(input('Please enter a positive integer : '))

# In line 9 we create an empty List to track the colllatz sequence
# Once the USER enters a positive integer it is assigned to the variable number.
# Then in line 10 we use append to add the value in the variable number to the collatzsequence LIST. 
# I decided to use a List to keep track of the sequence of numbers so I can print them afterwards 
collatzSequence = []
collatzSequence.append(number)

# While loop which keeps looping until the variable nummber goes to one.
# In the IF/ELSE statement we check if the number is ODD or EVEN and apply the relevant formula.
# We check if the number is ODD or EVEN by using the modulus operator and if there is no remainder we divide the number by 2 and append to List
# In the ELIF we check if there is a remainder and if there is a remainder we multiply the number by 3 and add 1, then we append to the List  
# The While loop will keep looping while number != 1 but once nummber == 1 the condiftion will be FALSE and the while loop will stop.  
while number != 1:
    if number % 2 == 0:
        number = number // 2
        collatzSequence.append(number)
    elif number % 2 == 1:
        number = (number * 3) + 1
        collatzSequence.append(number)

# We assign an empty STRING to collatzOutput
# We need to print out the sequence of numbers so we iterate over the collatzSequence List
# and we append it to the STRING collatzOutput.
# We use the str() function to convert the integer num to a sting and we add a space with " "
collatzOutput = ""
for num in collatzSequence:
    collatzOutput += str(num) + " " 

# Print out the STRING collatzOutput which has the Collatz sequence for the number entered by the USER
print(collatzOutput)

    



