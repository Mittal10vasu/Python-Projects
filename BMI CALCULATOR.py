def calculate_bmi(weight, height):
    """Calculate the BMI given weight in kg and height in meters."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def get_valid_input(prompt, min_value, max_value):
    """Get valid numerical input from the user within a specified range."""
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def main():
    print("Welcome to the BMI Calculator")

    weight = get_valid_input("Enter your weight in kilograms (kg): ", 10, 300)
    height = get_valid_input("Enter your height in meters (m): ", 0.5, 2.5)

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {category}")


if __name__ == "__main__":
    main()
