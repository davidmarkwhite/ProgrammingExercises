def getUnits():
  inputString = input("What units would you like to use (feet or meters)? ")
  if inputString == "feet" or inputString == "meters":
    return inputString
  return getUnits()

def getNumeric(dimension, units):
  try:
    return int(input("What is the {0} of the room in {1}? ".format(dimension,units)))
  except ValueError:
    return getNumeric(dimension)
  
def conversionFactor():
  return 0.09290304

def printMessage(length,width,units,areaFeet,areaMeters):
  print("You entered dimensions of {0} {1} by {2} {1}.".format(length,units,width))
  print("The area is")
  print("{0} square feet".format(str(areaFeet)))
  print("{0} square meters".format(str(areaMeters)))

def CalculateArea(length,width,units,returnUnits):
  if units == returnUnits:
    return length * width
  if units == "feet":
    return round(length * width * conversionFactor(),3)
  return round(length * width / conversionFactor(),3)
    
class AreaCalculator():
  units = getUnits()
  length = getNumeric("length",units)
  width = getNumeric("width",units)
  areaFeet = CalculateArea(length,width,units,"feet")
  areaMeters = CalculateArea(length,width,units,"meters")
  printMessage(length,width,units,areaFeet,areaMeters)

