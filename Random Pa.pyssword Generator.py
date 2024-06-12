import random
import string


def generate_password(length, include_letters, include_numbers, include_symbols):
    """Generate a random password based on user-defined criteria."""
    character_pool = ''
    if include_letters:
        character_pool += string.ascii_letters
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password


def get_user_input(prompt):
    """Get yes/no input from the user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")


def get_valid_length(prompt):
    """Get valid password length input from the user."""
    while True:
        try:
            length = int(input(prompt))
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def main():
    print("Welcome to the Password Generator")

    length = get_valid_length("Enter the desired password length: ")

    include_letters = get_user_input("Include letters? (y/n): ")
    include_numbers = get_user_input("Include numbers? (y/n): ")
    include_symbols = get_user_input("Include symbols? (y/n): ")

    try:
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
