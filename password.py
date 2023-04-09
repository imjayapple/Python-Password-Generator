# String module provides a collection of constants and functions related to string manipulation & processing
import string
# Random module provides a variety of functions for generating random numbers & making random selections
import random

def generate_password(length, include_punctuation):
    characters = string.ascii_letters + string.digits
