""""2. Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides, determine if the triangle is equilateral
(all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.

3 Input

side 1, side 2 and side 3

output - Eq, Iso, Scalene -

Eq. = side 1 == side 2 = side 3"""

side1 = float(input("enter 1st side of Triangle: "))
side2 = float(input("enter 2nd side of Triangle: "))
side3 = float(input("enter 3rd side of Triangle: "))

if side1 == side2 == side3:
    print("Triangle is equilateral")
elif side1 == side2:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")




















