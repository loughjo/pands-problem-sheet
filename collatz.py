#
# Author John Loughnane

number = int(input('Enter a positive integer : '))

aList = []
aList.append(number)
while number != 1:
    if number % 2 == 0:
        number = number // 2
        aList.append(number)
    elif number % 2 == 1:
        number = (number * 3) + 1
        aList.append(number)
print(*aList)
