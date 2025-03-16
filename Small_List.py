def find_smallest_with_min(numbers):
    
    if not numbers:
        return "List is empty!"
    return min(numbers)

# Example usage
numbers = [3, 1, 4, 1, 5, -9, 2]
print(f"The smallest number is: {find_smallest_with_min(numbers)}")  # Output: -9
