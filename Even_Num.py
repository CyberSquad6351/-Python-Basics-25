def find_even_numbers(numbers):
   
    return [num for num in numbers if num % 2 == 0]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Even numbers: {find_even_numbers(numbers)}")  # Output: [2, 4, 6, 8, 10]
