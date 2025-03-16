# Function to find the sum of even factors of a number
def sum_of_even_factors(num):
    sum_even_factors = 0
    
    # Iterate through all possible factors of num
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:  # Check if i is an even factor
            sum_even_factors += i
    
    return sum_even_factors

# Example number
num = 36

# Get the sum of even factors
result = sum_of_even_factors(num)

# Print the result
print("Sum of even factors of", num, "is:", result)
