import math;

print("Enter two numbers to see all the prime numbers between them");
# Continue loop while inputs are not valid
while True: 
	# Read in minimum number
	# Continue loop while input is not valid
	while True:
		# Read input as string
		s_min = raw_input("Enter a minimum number: ");
		# Attempt to convert input to a number 
		try:
			min = int(s_min);
			# If number is greater than zero then break out of loop
			if(min > 0):
				break;
			print("Please enter a number greater than zero");
		except:
			print("Please enter a valid number");
	# Read in maximum number		
	while True:
		s_max = raw_input("Enter a maximum number: ");
		try:
			max = int(s_max);
			if(max > 0):
				break;
			print("Please enter a number greater than zero");
		except:
			print("Please enter a valid number");
			
	# check that minimum number is less than maximum number
	if(min > max):
		print("Minimum cannot be greater than maximum");
	# check that numbers are different
	elif(min == max):
		print("Minimum and maximum must be different");
	else:
		break;
	
# list to store prime numbers
primeNumbers = [];
# loop through each number from the minimum up to the maximum
for i in range(min, max+1):
	# if number is even
	if(i%2 == 0):
		# if number is 2 then add it to the list of prime numbers
		if(i == 2):
			primeNumbers.append(i);
	# else number is odd
	else:
		# if number is 1 then add it to the list of prime numbers
		if(i == 1):
			primeNumbers.append(i);
		else:
			# calculate the square root of the number 
			sqRoot = math.sqrt(i);
			# check that the square root is not the square of another number 
			if(sqRoot != math.floor(sqRoot)):
				# floor it to ensure it is a whole number 
				sqRoot = math.floor(sqRoot);
				# variable to determine whether or not number is prime 
				isPrime = True;
				# start at 3 and continue up to the square root 
				for j in range(3, int(sqRoot)+1):
					# if j divides evenly into i then it is not prime so break out of loop
					if(i%j == 0):
						isPrime = False;
						break;
				# if number is still prime then add it to the list of prime numbers
				if isPrime:
					primeNumbers.append(i);
				
# show the total number of prime numbers				
print("There are %d prime numbers between %d and %d " % (len(primeNumbers), min, max));			
# print each prime number 
for i in primeNumbers: 
	print(i),