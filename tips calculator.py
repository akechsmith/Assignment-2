# Input the total bill amount
total_bill = float(input("Enter the total bill amount: "))

# Input the tip percentage (10%, 12%, or 15%)
tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))

# Input the number of people splitting the bill
num_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the tip amount
tip_amount = (tip_percentage / 100) * total_bill

# Calculate the total amount to be paid
total_amount = total_bill + tip_amount

# Calculate the amount each person should pay
amount_per_person = total_amount / num_people

# Display the result rounded to two decimal points
print(f"Each person should pay: ${amount_per_person:.2f}")
