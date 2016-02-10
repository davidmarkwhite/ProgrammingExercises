import string, tkinter
from tkinter.constants import *
from tkinter import *

class AreaCalculatorUI():

  def __init__(self):
    self.tk = tkinter.Tk()

    self.units = tkinter.StringVar()
    self.length = tkinter.StringVar()
    self.width = tkinter.StringVar()
    self.areaFeet = tkinter.StringVar()
    self.areaMeters = tkinter.StringVar()

    self.units.set("feet")
    self.length.set("0")
    self.width.set("0")

    self.units.trace("w",self.recalculate)
    self.length.trace("w",self.recalculate)
    self.width.trace("w",self.recalculate)

    frame = tkinter.Frame(self.tk, relief=RIDGE, borderwidth=2)
    frame.pack()

    unitsLabel = tkinter.Label(frame,text="Please select a unit")

    feetRadio = Radiobutton(frame, text="Feet", variable=self.units, value="feet")
    feetRadio.pack()
    metersRadio = Radiobutton(frame, text="Meters", variable=self.units, value="meters")
    metersRadio.pack()

    lengthLabel = tkinter.Label(frame, text="What is the length?")
    lengthLabel.pack()
    lengthEntry = tkinter.Entry(frame, textvariable=self.length)
    lengthEntry.pack()

    widthLabel = tkinter.Label(frame, text="What is the width?")
    widthLabel.pack()
    widthEntry = tkinter.Entry(frame, textvariable=self.width)
    widthEntry.pack()

    areaFeetLabel = tkinter.Label(frame, text="Area in feet:")
    areaFeetLabel.pack()
    areaFeetOutput = tkinter.Label(frame, textvariable=self.areaFeet)
    areaFeetOutput.pack()

    areaMetersLabel = tkinter.Label(frame, text="Area in meters:")
    areaMetersLabel.pack()
    areaMetersOutput = tkinter.Label(frame, textvariable=self.areaMeters)
    areaMetersOutput.pack()

    self.tk.mainloop()

  def recalculate(self,*args):
    if self.units.get() == "meters":
      self.areaMeters.set(str(int(self.length.get()) * int(self.width.get())))
      self.areaFeet.set(str(round(float(self.areaMeters.get()) / self.conversionFactor(),3)))
    else:
      self.areaFeet.set(str(int(self.length.get()) * int(self.width.get())))
      self.areaMeters.set(str(round(float(self.areaFeet.get()) * self.conversionFactor(),3)))

  def conversionFactor(self):
    return 0.09290304

AreaCalculatorUI()
