# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print prime numbers in a given interval
def print_primes_in_interval(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Example interval
start = 10
end = 50

# Print prime numbers in the interval
print("Prime numbers between", start, "and", end, "are:")
print_primes_in_interval(start, end)
