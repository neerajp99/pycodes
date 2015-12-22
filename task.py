#!/usr/bin/env python

"""
Simple Python program
which asks for a Question
"""

# Main Function
def main ():

	try:
		num = int(input("Question: Enter a number between 1 - 20: "))
		if num > 10 and num < 21:
			print ("The entered number lies between 10 - 20")
		elif num >0 and num < 11:
			print ("The entered number lies between 1 - 10")
		else:
			print ("Enter a valid number in the range")
	except ValueError:
		print("Please enter a valid number !")

if __name__ == '__main__':
	main()