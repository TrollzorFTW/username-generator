#!/usr/bin/python3
import argparse
from combinations import *

def get_users(user_file):
	with open(user_file,"r",encoding="utf-8") as uf:
		users = [u.strip() for u in uf.readlines()]

	return users


def generate_combinations(users):
	generated_users = []

	for user in users:

		first_name,last_name = user.split(' ')[0],user.split(' ')[1]
		generated_users += first_combination(first_name,last_name) + second_combination(first_name,last_name) + third_combination(first_name,last_name)
	
	return generated_users

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--userlist",help="User list separated by newlines",required=True)
	parser.add_argument("-o","--output",help="File to output the result",required=True)

	userlist = parser.parse_args().userlist	
	output = parser.parse_args().output
	
	users = get_users(userlist)
	generated_users = generate_combinations(users)
	
	with open(output,'w',encoding='utf-8',newline='') as outfile:
	
		for user in generated_users:
			outfile.write(user+'\n')

if __name__ == '__main__':
	main()
