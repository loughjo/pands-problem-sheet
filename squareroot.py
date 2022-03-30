
# Author : John Loughnane

num = int(input("Enter a number : "))

squareroot = 1
y = 1

while y**2 != num:
    num1 = (squareroot**2)-2
    print()
    num2 = 2*squareroot
    print("num 2 :",)
    num3 = squareroot - (num1/num2)
    squareroot = num3
    y = num3
    
    print("internal",squareroot)

print(squareroot)
