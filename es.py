#Author : John Loughnane

# https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python

import sys

with open(sys.argv[1]) as filename:
    count = 0
    not_e = 0

# First iterate over filename and each line is assigned to variable line which will be of type STRING.
# The variable line is then      
    for line in filename:
        string_name = ""
        string_name = line
        for char in string_name:
            if char == "e":
                count += 1
            else:
                not_e += 1

print(count)