# Write a program that asks the user to input any positive integer and then calculates and outputs the collatz sequence
# Author John Loughnane

# Asks the user to enter a positive integer and converts the String input to and integer and assigns it to a variable called number
number = int(input('Please enter a positive integer : '))

collatzSequence = []
collatzSequence.append(number)
while number != 1:
    if number % 2 == 0:
        number = number // 2
        collatzSequence.append(number)
    elif number % 2 == 1:
        number = (number * 3) + 1
        collatzSequence.append(number)

collatzOutput = ""
for num in collatzSequence:
    #print(num)
    collatzOutput += str(num) + " " 
     
print(collatzOutput)
    


#print(*collatzSequence)
