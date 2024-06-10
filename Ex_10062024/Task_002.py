# Task 2

# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

num = 2
square_num = num**2
print("Square of Num is : ", square_num)

cube_num = num**3
print("Cube of Num is : ", cube_num)

'''
Create a program that takes two numbers as input and prints whether the first number is greater than, less than, 
or equal to the second number. '''

num1 = int(input("enter first num: "))
num2 = int(input("enter second num: "))

if num1 > num2:
    print(f"first num = {num1} is greater")
elif num1 < num2:
    print(f"second num = {num2} is greater")
elif num1 == num2:
    print("both nums are equal")
elif num1 < num2:
    print(f"first num = {num1} is less")
else:
    print(f"second num = {num2} is less",)
