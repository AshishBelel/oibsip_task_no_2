import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    try:
        length = int(input("Enter the length of the password: "))
        use_letters = input("Include letters? (y/n): ").lower() == "y"
        use_numbers = input("Include numbers? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")
        return

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("Your random password is:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
