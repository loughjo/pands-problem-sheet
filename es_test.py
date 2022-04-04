#Author : John Loughnane

# https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python

import sys

with open(sys.argv[1]) as filename:
    count = 0
    not_e = 0

# First iterate over filename and each line is assigned to variable line which will be of type STRING.
# We then need to iterate over the STRING line in order to find each 'e' character
# we iterate over line and assign each letter to the variable char in turn. 
# In the IF statement if char == "e" is TRUE we incremant the integer count by 1.      
    for line in filename:
        for char in line:
            if char == "e":
                count += 1
                #print("count " + char)
            else:
                not_e += 1

# Print out the number of 'e' letters found in the file 
print(count)