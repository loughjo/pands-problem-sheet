# Write a program that asks a user to input a string and outputs every second letter in reverse order.
# Author : John Loughnane

# Use the input method to enter in a sentence and assign it to a String variable called sentence
sentence = input("Please enter a sentence : ")

# Takes in a string and use the slice function to output every second letter in reverse order.
# To do that we need to use the syntax = [::-2] where -2 will step backwards and output every second character
# We assign the value to reverseSentence which which will be of type STRING.
reverseSentence = sentence[::-2]

# print out the contents of the reverseSentence string variable.
print(reverseSentence)