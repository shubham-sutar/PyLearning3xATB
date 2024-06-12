# Task - Fibonacci series


num = int(input("enter any num: "))

val1 = 0
val2 = 1

for i in range(0, num+1):
    if i <= 1:
        print(i)
    else:
        result = val1 + val2
        val1 = val2
        val2 = result
        print(result)







