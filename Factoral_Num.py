def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Prompting the user for input
try:
    user_input = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {user_input} is: {factorial_iterative(user_input)}")
except ValueError:
    print("Invalid input! Please enter an integer.")
