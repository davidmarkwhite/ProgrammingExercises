import string, tkinter
from tkinter.constants import *

class StringLengthUI():

	def __init__(self):
		self.tk = tkinter.Tk()
		self.inputString = tkinter.StringVar()
		self.outputString = tkinter.StringVar()
		self.inputString.trace("w",self.recalculate)

		frame = tkinter.Frame(self.tk, relief=RIDGE, borderwidth=2)
		frame.pack()
		inputLabel = tkinter.Label(frame, text="What is the input string?")
		inputLabel.pack()
		inputEntry = tkinter.Entry(frame, textvariable=self.inputString)
		inputEntry.pack()
		outputLabel = tkinter.Label(frame, textvariable=self.outputString)
		outputLabel.pack()

		self.tk.mainloop()

	def recalculate(self, *args):
		self.outputString.set(self.inputString.get() + " has " + str(len(self.inputString.get())) + " characters.")

StringLengthUI()