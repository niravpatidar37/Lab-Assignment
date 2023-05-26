def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Input principal amount, rate of interest, and time in years
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Print the result
print("Simple Interest:", simple_interest)
