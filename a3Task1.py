def factorial():
    n = int(input("Enter a number2: "))


    if n < 0:
        return n,"not defined"
    if n == 0 or n == 1:
        return n, 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return n, result

#printing the result

num, factorial_result = factorial()
print(f"The factorial of {num} is: {factorial_result}")
