#!/usr/bin/python
import Tkinter
from Tkinter import *
from tkFileDialog import askopenfilename
import vendorEmailRedirect

class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.instructionVariable = Tkinter.StringVar()
		self.instruction =Tkinter.Label(self,textvariable=self.instructionVariable)
		self.instruction.grid(column=0,row=0,sticky='EW')

		self.instructionVariable.set("Choose the vendor redirect email spreadsheet :")
		button = Tkinter.Button(self,text=u"Open",command = self.OnButtonClick)
		button.grid(column=1,row=0)

		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable,anchor="w",fg="white",bg="blue")
		label.grid(column=0,row=1,columnspan=2,sticky='EW')
		self.labelVariable.set("Hello")
		
		self.text = Tkinter.Text(self)
		self.text.grid(column=0,row=2,columnspan=2,sticky='EW')

		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,False)

	def OnButtonClick(self):
		self.choosen = askopenfilename(initialdir='~')
		self.labelVariable.set(vendorEmailRedirect.parseFile(self.choosen))
		self.text.insert(END,vendorEmailRedirect.parseFile(self.choosen))
if __name__=="__main__":
	app = simpleapp_tk(None)
	app.title('Vendor Email Redirector')
	app.mainloop()
	