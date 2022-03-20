# Write a program that asks a user to input a string and outputs every second letter in reverse order.
# Author : John Loughnane

# https://stackoverflow.com/questions/58886774/python-how-do-i-reverse-every-other-string-in-a-list (reverse a string)
# https://www.w3schools.com/python/python_howto_reverse_string.asp

# Use the input method to enter in a sentence and assign it to a String variable called sentence
sentence = input("Please enter a sentence : ")

# Takes in a string and use the slice function to output every second letter in reverse order.
# To do that we need to sue the syntax = [::-2] where -2 will step backwards and output every second character 
reverseSentence = sentence[::-2]

# print out the contents of the reverseSentence string variable.
print(reverseSentence)