# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to determine weight status based on BMI
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main program to get user input and calculate BMI
def main():
    # Input weight and height from the user
    weight = float(input("Enter your weight in (kg): "))
    height = float(input("Enter your height in (m): "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Get BMI category
    category = get_bmi_category(bmi)
    
    # Output the results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the “{category}” range.")

# Run the program
if __name__ == "__main__":
    main()
