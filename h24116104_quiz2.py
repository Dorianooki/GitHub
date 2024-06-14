money = int(input("Enter the shopping amount:"))
membership = input("Enter the membership level(Regular or Gold): ")
if membership == "Regular":
	if 1000>=money>0:
		print(membership, "$", money)
	if 2000>=money>1000:
		print(membership, "$", 0.9*money)
	if 3000>=money>2000:
		print(membership, "$", 0.85*money)
	if money>3000:
		print(membership, "$", 0.8*money)

elif membership == "Gold":
	if 1000>=money>0:
		print(membership, "$", money)
	if 2000>=money>1000:
		print(membership, "$", 0.85*money)
	if 3000>=money>2000:
		print(membership, "$", 0.8*money)
	if money>3000:
		print(membership, "$", 0.75*money)

else:
	print("Invalid membership level, Please enter 'Regular' or 'Gold'")
