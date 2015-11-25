class stringLength():
	string = input("What is the input string? ")
	while string == "":
		string  = input("Please enter an input string. ")
	print(string + " has " + str(len(string)) + " characters")