def compound_interest(principal, rate, times_compounded, years):
    
    total_amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    return total_amount

# Prompting the user for input
try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    times_compounded = int(input("Enter the number of times interest is compounded per year: "))
    years = int(input("Enter the number of years: "))

    total_amount = compound_interest(principal, rate, times_compounded, years)
    print(f"The total amount after {years} years is: {total_amount:.2f}")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
