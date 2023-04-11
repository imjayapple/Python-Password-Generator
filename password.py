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

def main():
    print("Welcome to the Random Password Generator!")
