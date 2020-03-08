country = input ("Which country are you from?")
age = input ("Please input your age: ")
age = int(age)
if country == "taiwan":
	if age >= 18:
		print("you can go to take driving exam")
	else:
		print("you can't take the driving exam yet")