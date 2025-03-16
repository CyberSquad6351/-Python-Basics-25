# Function to find the common divisors of two numbers
def common_divisors(num1, num2):
    # Find the minimum of the two numbers to reduce the number of iterations
    min_num = min(num1, num2)
    
    # List to store common divisors
    common_divisors_list = []
    
    # Loop through all numbers from 1 to the minimum of the two numbers
    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors_list.append(i)
    
    return common_divisors_list

# Example numbers
num1 = 12
num2 = 18

# Get the common divisors
divisors = common_divisors(num1, num2)

# Print the common divisors
print("Common divisors of", num1, "and", num2, "are:", divisors)
