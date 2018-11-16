'''
I just learned how to use regular expressions. So, this is just a little test program
on what I learned.

The user is prompted to input a string with the format xxx-xxx-xxxx. The x values must be numbers.
If the input matches the the regex pattern, then the input is printed to the screen. If it contains
letters, an error message is printed. And else, it will print the default error message.

Created on: 2018-11-15
'''
import re

phone_pattern = r"^\d\d\d-\d\d\d-\d\d\d\d$"

def check_number(input_string):
	if re.match(phone_pattern, input_string):
		print("\nPhone number: {}".format(input_string))
	elif re.search(r"[a-zA-Z]", input_string):
		print("\nInvalid format: Phone number cannot contain letters")
	else:
		print("\nInvalid format")

check_number(input("Enter phone number (xxx-xxx-xxxx): "))
