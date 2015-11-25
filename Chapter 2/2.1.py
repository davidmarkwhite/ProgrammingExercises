class SayHello():
	name = input("What is your name? ")
	greeting = "Hello, " + name + ", nice to meet you!"
	print(greeting)

class SayHelloWithoutVariables():
	print("Hello, " + input("What is your name? ") + ", nice to meet you!")