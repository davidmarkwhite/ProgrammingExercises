import string, tkinter
from tkinter.constants import *

class SimpleMathUI():

	def __init__(self):
		self.tk = tkinter.Tk()
		self.num1 = tkinter.StringVar()
		self.num2 = tkinter.StringVar()
		self.outputString = tkinter.StringVar()
		self.num1.trace("w",self.recalculate)
		self.num2.trace("w",self.recalculate)
		frame = tkinter.Frame(self.tk, relief=RIDGE, borderwidth=2)
		frame.pack()
		num1Label = tkinter.Label(frame, text="What is the first number?")
		num1Label.pack()
		num1Entry = tkinter.Entry(frame, textvariable=self.num1)
		num1Entry.pack()
		num2Label = tkinter.Label(frame, text="What is the second number?")
		num2Label.pack()
		num2Entry = tkinter.Entry(frame, textvariable=self.num2)
		num2Entry.pack()
		outputLabel = tkinter.Label(frame, textvariable=self.outputString)
		outputLabel.pack()
		self.tk.mainloop()

	def isValidInput(self, string):
		try:
			num = int(string)
			return num > 0
		except ValueError:
			return False

	def recalculate(self, *args):
		if self.isValidInput(self.num1.get()) and self.isValidInput(self.num2.get()):
			num1 = int(self.num1.get())
			num2 = int(self.num2.get())
			sum = num1 + num2
			difference = num1 - num2
			product = num1 * num2
			quotient = int(num1 / num2)
			self.outputString.set("{0} + {1} = {2} \n{0} - {1} = {3} \n{0} * {1} = {4} \n{0} / {1} = {5}".format(str(num1), str(num2), str(sum), str(difference), str(product), str(quotient)))

SimpleMathUI()