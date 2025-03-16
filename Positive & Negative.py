# Function to separate positive and negative numbers in a list
def separate_positive_negative(numbers):
    positive_numbers = []
    negative_numbers = []
    
    # Iterate through the list and classify numbers
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negative_numbers.append(num)
    
    return positive_numbers, negative_numbers

# Example list
numbers = [5, -3, 7, -2, 0, -8, 4]

# Get the positive and negative numbers
positives, negatives = separate_positive_negative(numbers)

# Print the results
print("Positive numbers:", positives)
print("Negative numbers:", negatives)
