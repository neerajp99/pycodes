#!/usr/bin/python

'''
Simple Python program
which asks for a Question
'''

# Main Function
def main ():	
	num = int(input("Question: Enter a number between 1 - 20: "))

	# prints a statement based on a query
	if num > 10:
		print ("The entered number is greater than 10")
	else:
		print ("The entered number lies between 1 - 10")

if __name__ == '__main__':
	main()