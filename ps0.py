# function 0
''' boolean function that takes in a positive integer or zero as a parameter and returns whether the number even or not '''

def is_number_even(integer): # define the function, it takes 1 parameter 
	if integer % 2 == 0:	 # if there is no remainder when dividing the number by 2, it is even
		return True			 # returns True because it is true that the number is even
	else: 					 # if the number is not divisible by 2, it must be odd
		return False		 # returns False since the number is not even
	
	
# function 1
''' takes a non-negative integer as a parameter and returns the number of digits in it ''' 

def number_of_digits(integer): # define function, it takes 1 parameter
	integer = str(integer)	   # converts the integer to a string (all digits are now characters) so its length can be measured
	length = len(integer) 	   # finds the length of the string the integer was converted to
	return length			   # returns the length, which is how many characters are in the string and therefore how many digits are in the integer 
	
	
# function 2
''' takes a non-negative integer as a parameter and returns the sum of its digits '''

def sum_of_digits(integer):						# define the function, it takes 1 parameter
	integer = str(integer) 						# converts the integer to a string so its length can be found
	lengthInteger = len(integer)				# finds the length (how many digits are in it) of the integer
	counter = 0									# keeps the loop going until it has taken all the digits of the integer into account
	totalSum = 0								# adds up all the digits as the loop is being run
	while lengthInteger != counter: 			# runs the loop while all digits have not been added up yet
		currentDigit = int(integer[counter])	# identifies the digit the program is currently looking at and converts it to an integer so it can be added to all the other digits in the integer
		totalSum += currentDigit				# adds the digit that was being looked at to the rest of the digits that have been looked at
		counter += 1							# increases the counter by 1 to look at the next digit in the integer

	return totalSum								# returns the sum of the digits once the loop has finished running and all the digits in the integer were added up 
	
	
# function 3
''' takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number '''

def sum_less_ints(integer):						# define the function
	sumInts = 0									# sets variable that will collect all the numbers less than integer
	for x in range(integer - 1):				# loops through consecutive numbers less than integer
		sumInts += (x + 1)						# adds the number to sumInts, adds one to x because x starts at 0
	return sumInts								# when the loop is finished, the sum of all the numbers less than the int is returned
		
	
# function 4	
''' takes a non-negative integer as a parameter and returns its factorial '''

import operator															 # imports to later use in the function
import functools

def factorial(integer):													 # define the function, it takes 1 parameter
	counter = 1															 # keeps track of the next number that is to be multiplied
	totalProduct = 1												 	 # keeps track of all the numbers being multiplied together to find the factorial
	while counter <= integer: 										 	 # keeps the loop running while the next integer is not greater than the integer that is the parameter 
		totalProduct = totalProduct * counter							 # multiplies new counter value to the product of the rest of the counter values
		counter += 1													 # increments the counter by one to prepare to multiply the next integer
	return totalProduct												     # returns what the factorial of the integer is


# function 5
''' boolean function that takes two positive integers as parameters and figures out whether the second number is a factor the first '''

def is_it_a_factor(integer, factor): # defines the function, it takes 2 parameters
	if factor == 0: 
		return "you cannot divide a number by 0"
	if integer % factor == 0: 		 # runs if their is no reminder when diving integer by factor
		return True					 # returns true, because if their is no remainder, the integer is divisible by the factor and the factor is in fact a 
	else: 							 # runs if the remainder of the two is not 0
		return False				 # if the remainder is not 0, their is a remainder, so it is not a factor and the function returns False

	
# function 6
''' boolean function that takes a positive integer as a parameter and returns whether the number is a prime '''

def prime(integer):							# define the function, it takes 1 parameter
	if integer == 1: 						# returns a specific statement if the integer is 1, because it is a special case
		return "1 is niether prime nor composite, it is a special case"
	counter = 2								# keeps track of the number that the integer is being divided by (starts at 2 because all integers can be divided by 1) 
	while counter < integer: 				# loop runs while counter is less than the integer, because you don't need to divide the integer by itself
		divideTest = integer % counter		# keeps track of the remainder of integer divided by counter
		if divideTest == 0: 				# if the remainder is 0 the counter divided into integer evenly 
			return False					# it returns False because once the integer is divisible by another integer, it is not prime
		else: 								# else, there is a remainder
			pass							# the loop passes to incrementing the counter so the loop can keep running and checking if the integer is divisible by anything
		counter += 1						# increments counter to divide the integer by the next number
		
	return True								# once the loop is finished running and there was always a remainder when the integer was being divided, the number is prime and True is returned
		

# function 7
''' boolean function that takes a positive integer as a parameter and tells whether the number is perfect '''

def is_perfect(integer): 					# define the function, it takes 1 parameter 
	if integer == 0: 						# if the integer is 0, True and statement for special case is returned
		return "True, because 0 = 0 "		
	counter = 1								# keeps track of the integers to add together
	totalSum = 0							# adds up all the integers
	listToPrint = ""						# keeps track of all the integers that have been added up to print at the end
	while counter < integer: 				# keeps loop running while counter is less than the integer, because a proper factor is not a factor of itself
		if integer % counter == 0: 			# if there is no remainder, counter is a factor of the integer 
			if len(listToPrint) != 0: 	    # adds a plus sign to the string, if the string is not empty (so it won't print "+ 1")
				listToPrint += " + "		
			listToPrint += str(counter)		# adds counter to the listToPrint as well 
			totalSum += counter				# adds the current value of counter to totalSum 
		counter += 1						# increments counter by 1 so the next factor can be found
	if totalSum == integer: 				# if the totalSum equals the integer, it is a perfect number
		return ("True, because {} = ".format(integer) + listToPrint) # returns True, and the properly formatted statement 
	else: 									# if totalSum never equals the integer, it is not a perfect number and False is returned
		return False
		

# function 8	
''' boolean function that takes a positive integer as a parameter and returns true if the sum of the digits of the number divides evenly into the number, false otherwise '''
	
def does_sum_digits_divides_number(integer): 	# define the function, takes 1 parameter
	sumDigitsFunction = sum_of_digits(integer)  # call previous function and set it to a variable
	if integer % sumDigitsFunction == 0: 		# runs if the integer is divisible by the sum of the intigers digits
		return True								# returns true if there is no remainder 
	else: 										# returns false if there is a remainder and the integer is not divisible by its digits
		return False
		
