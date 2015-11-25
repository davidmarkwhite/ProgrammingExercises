import string, tkinter
from tkinter.constants import *

class TipCalculator(object):

	def getValidFloat(inputVar,errorVar):
		try:
			returnAmount =  float(inputVar.get())
		except ValueError:
			returnAmount = 0
			inputVar.set("0.00")
			errorVar.set("Please enter a valid number")
		if returnAmount < 0:
			returnAmount = -returnAmount
			inputVar.set('%.2f' % returnAmount)
		else:
			errorVar.set("")
		return returnAmount

	def calculateTip(billAmount,tipPercentage):
		return billAmount * tipPercentage / 100

	def calculateTotal(billAmount,tipAmount):
		return billAmount + tipAmount


class TipCalculatorUI():

	def __init__(self):
		self.tk = tkinter.Tk()
		self.error = tkinter.StringVar()
		self.billAmount = tkinter.StringVar()
		self.tipPercentage = tkinter.StringVar()
		self.tipAmount = tkinter.StringVar()
		self.total = tkinter.StringVar()
		self.drawScreen()
		self.tk.mainloop()

	def drawScreen(self):
	
		frame = tkinter.Frame(self.tk, relief=RIDGE, borderwidth=2)
		frame.pack()

		billLabel = tkinter.Label(frame, text="What is the bill amount?")
		billLabel.pack()

		self.billAmount.set("0.00")
		self.billAmount.trace("w",self.recalculate)
		billInput = tkinter.Entry(frame, textvariable=self.billAmount)
		billInput.pack()

		tipPercentLabel = tkinter.Label(frame, text="What is the tip percentage?")
		tipPercentLabel.pack()
		
		self.tipPercentage.set("0.00")
		self.tipPercentage.trace("w",self.recalculate)
		tipPercentInput = tkinter.Entry(frame, textvariable=self.tipPercentage)
		tipPercentInput.pack()
		
		self.tipAmount.set("The tip is $0.00")
		tipAmountLabel = tkinter.Label(frame, textvariable=self.tipAmount)
		tipAmountLabel.pack()
		
		self.total.set("The total is $0.00")
		totalLabel = tkinter.Label(frame, textvariable=self.total)
		totalLabel.pack()

		errorLabel = tkinter.Label(frame, textvariable=self.error, fg="red")
		errorLabel.pack()

	def recalculate(self, *args):
		billAmount = TipCalculator.getValidFloat(self.billAmount, self.error)
		tipPercent = TipCalculator.getValidFloat(self.tipPercentage, self.error)
		tipAmount = TipCalculator.calculateTip(billAmount,tipPercent)
		self.tipAmount.set("The tip is $%.2f" % tipAmount)
		self.total.set("The total is $%.2f" % TipCalculator.calculateTotal(billAmount,tipAmount))

TipCalculatorUI()