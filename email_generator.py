'''
Created on 2018-11-16 by Gabriel Hooks
'''

import string
import random

first_names = ["Gabriel", "George" "Ashley", "Molly", "Greg", "Gavin", "Josh", "John", 
 "Jack", "Travis", "Tyler", "Peter", "Will", "Xavier", "Frederick", "Frank", "Caleb", 
 "Melanie", "Matthew", "Logan", "David", "Joanne", "Steven", "Stephen", "Steve"]

last_names = ["Hooks", "Smith", "Jones", "Brown", "Davis", "Miller", "Moore", "Taylor", 
 "Hill", "Scott", "King", "Hernandez", "Gomez", "Reed", "Cook", "Green", "Washington",
 "Rivera", "Cox", "Zilli", "Finoli", "Bush", "Six", "Adams", "Torres"]

domains = ["@gmail.com", "@live.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@gslions.net"]

addresses = []

def gen_rand_address(count):
	for i in range(count):
		local_part_len = random.randrange(6, 16)
		# Create randomized string for local-part
		address = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(1, local_part_len)])
		# Append one of the domains to the end of address
		address += random.choice(domains)
		
		addresses.append(address)
	return addresses
	
def gen_legit_address(count):
	for i in range(count):
		# Append first name
		address = ''.join(random.choice(first_names))
		# Append last name
		address += random.choice(last_names)
		# Append random 1 or 2 digit number for diversity
		address += str(random.randrange(0, 100))
		# Append one of the domains to the end of address
		address += random.choice(domains)
		
		addresses.append(address)
	return addresses

print(gen_legit_address(20))
