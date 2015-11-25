import time
class RetirementCalculator(object):
	currentAge = input("What is your current age? ")
	retirementAge = input("At what age would you like to retire? ")
	yearsLeft = int(retirementAge) - int(currentAge)
	currentYear = time.strftime("%Y")
	retirementYear = int(currentYear) + yearsLeft
	if yearsLeft > 0:
		print("You have " + str(yearsLeft) + " years left until you can retire.")
		print("It's " + currentYear + ", so you can retire in " + str(retirementYear) + ".")
	else:
		print("You can already retire.")		