stop = 1
game = ""
#print greeting words
print("Welcome to the simple calculator program !")

while stop == 1:
	#for users to entering the demanding value
	s1 = float(input("Enter the first number:"))
	s2 = float(input("Enter the second number:"))
	ao = input("Select an arithmetic operation(+, -, *, /):")
	#use while loops to calculate 
	while stop != 0:
		if ao == "+":
			print("Result:", s1+s2)
			stop = 0
			continue	
		elif ao == "-":
			print("Result:", s1-s2)
			stop = 0
			continue	
		elif ao == "*":
			print("Result:", s1*s2)
			stop = 0
			continue
		elif ao == "/":
			print("Result:", s1/s2)
			if s2 == 0:
				print("Error, division by zero")
				continue
			stop = 0
			continue
	
	while stop == 0:
		game = input("Do you want to perform another calculation?(yes or no): ")
		if game == "yes":
			stop = 1
			continue
		if game == "no":
			print("Goodbye!")
			exit()
















