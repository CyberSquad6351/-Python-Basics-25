def multiply_list(numbers):
    
    if not numbers:
        return 0 
    result = 1
    for num in numbers:
        result *= num
    return result


numbers = [2, 3, 4]
print(f"The product of the list is: {multiply_list(numbers)}")  