# Task - Fibonacci series and Factorial

fact_num = int(input("Enter any number: "))

store = 1
i = 1
while i <= fact_num:
    store = store * i
    i = i + 1

print(f"Factorial of {fact_num} is : {store}")