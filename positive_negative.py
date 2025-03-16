def count_positive_negative(numbers):
    positive_count = 0
    negative_count = 0
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    return positive_count, negative_count

# Example usage
numbers = [-10, 2, 3, -1, 4, -6, 0]
pos_count, neg_count = count_positive_negative(numbers)
print(f"Positive numbers: {pos_count}, Negative numbers: {neg_count}")
