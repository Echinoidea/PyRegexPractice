'''
Practicing regular expressions.

The user is prompted to input an email. If the inputted string follows the pattern, the email is
printed back onto the screen. Else, a default error message is printed.

Created on 2018-11-16 by Gabriel Hooks
'''

import re

pattern = r"([\w\.\-]+)@([\w\.\-]+)(\.[\w\.]+)"

def check_email(input_email):
	if re.match(pattern, input_email):
		print("Email = {}".format(input_email))
	else:
		print("Invalid input!")

check_email(input("Enter email: "))

