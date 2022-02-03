# 
# Author John Loughnane
# Write a program that asks a user to input a string and outputs every second letter in reverse order.

# Use the input method to enter in a sentence and assign it to the variable sentence
sentence = input("Please enter a sentence : ")

# Takes in a string and outputs every second letter in reverse order
a = sentence[::-2]
print(a)