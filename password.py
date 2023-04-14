# String module provides a collection of constants and functions related to string manipulation & processing
import string
# Random module provides a variety of functions for generating random numbers & making random selections
import random

# Function that accepts two parameters, length of password, & boolean for including punctuation in the password
# Concatenate a string with ascii letters & digits
# If-statement, include or exclude punctuation to characters
# Generate list comprehension, use the user-input for length and select out those characters from the
# characters string and ''.join them to create a new password 
def generate_password(length, include_punctuation):
    characters = string.ascii_letters + string.digits

    if include_punctuation:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# While loop to obtain valid input for desired PW length
# Minimum length of 4, if-else statement
# Include puncuation if desired, if not password will not include puncuation
def main():
    print("Welcome to the Random Password Generator!")

    while True:
        try:
            length = int(input("\nEnter the desired password length (minimum 4 characters): "))
            if length >= 4:
                break
            else:
                print("Invalid input. Please enter an integer greater than or equal to 4.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    include_punctuation = input("Do you want to include punctuation in your password? (Y/N): ").upper() == 'Y'

    password = generate_password(length, include_punctuation)
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()