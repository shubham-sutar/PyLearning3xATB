# condition and loop
# if , else

age = int(input("enter ur age"))

if age > 18:
    print("ur eligible for vote")
else:
    print("ur not eligible for vote")

# max

num1 = 12
num2 = 22
num3 = 46

max_num = max(num1, num2, num3)
print(max_num)

# for loop

for i in range(5):
    print(i)

# Range(start, stop, step)
for i in range(1, 10, 1):
    print(i)

# While loop

i = 0
while i < 5:
    print(i)
    i = i + 1


# multiple condition by using elif

score = int(input("enter ur grade: "))

if score >= 90 and score <= 100:
    print("grade A")
elif score >= 60 and score <= 89:
    print("grade B")
elif score >= 40 and score <= 59:
    print("grad c")
else:
    print("ur failed")
