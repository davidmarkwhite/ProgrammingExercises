class SimpleMath():
	def isValid(string):
		try:
			num = int(string)
			return num > 0
		except ValueError:
			return False

	num1 = input("What is the first number? ")
	while not isValid(num1):
		num1 = input("Please enter a positive number. ")

	num2 = input("What is the second number? ")
	while not isValid(num2):
		num1 = input("Please enter a positive number. ")

	sum = int(num1) + int(num2)
	difference = int(num1) - int(num2)
	product = int(num1) * int(num2)
	quotient = int(int(num1) / int(num2))

	print ("{0} + {1} = {2} \n{0} - {1} = {3} \n{0} * {1} = {4} \n{0} / {1} = {5}".format(num1, num2, str(sum), str(difference), str(product), str(quotient)))

