# Input weight (in kilograms) and height (in centimeters)
weight = int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in centimeters: "))

# Convert height to meters
height_meters = height / 100

# Calculate BMI
BMI = weight / (height_meters * height_meters)

# Determine BMI category
if BMI < 18:
    category = "Underweight"
elif 18 <= BMI < 25:
    category = "Normal weight"
else:
    category = "Overweight"

# Display the result
print(f"Your BMI is: {BMI:.2f}")
print(f"You are classified as: {category}")