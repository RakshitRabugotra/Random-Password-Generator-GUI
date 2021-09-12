import random
import pyperclip
from tkinter import *
from tkinter import ttk


TITLE = 'Random Password Generator'
# GEOMETRY = '400x400'
RESIZABLE = False


class Generator:
	def __init__(self, master):

		# Initializing all the Variables
		self.lengthVar = IntVar()
		self.Strength = IntVar()


		self.pass_label = Label(master, text='Password')

		self.e = Entry(master)

		self.generate_button = Button(master, text='Generate', command=self.generate)
		self.generate_button.config(relief=RAISED)

		self.copy_button = Button(master, text='Copy', command=self.copy)
		self.copy_button.config(relief=RAISED)

		self.clear_button = Button(master, text='Clear', command=self.clear)
		self.clear_button.config(relief=RAISED)

		self.length_label = Label(master, text='Length')
		self.combo = ttk.Combobox(master, textvariable=self.lengthVar)
		self.combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
								 17, 18, 19, 20, 21, 22, 23, 24, 25,
								 26, 27, 28, 29, 30, 31, 32)

		self.radio_low = Radiobutton(master, text='Low', variable=self.Strength, value=1)
		self.radio_med = Radiobutton(master, text='Medium', variable=self.Strength, value=2)
		self.radio_high = Radiobutton(master, text='High', variable=self.Strength, value=3)

		# Griding all the Widgets
		self.pass_label.grid(row=0, column=0)
		self.e.grid(row=0, column=1)

		self.generate_button.grid(row=0, column=2)
		self.copy_button.grid(row=0, column=3)
		self.clear_button.grid(row=0, column=4)

		self.length_label.grid(row=1, column=0)

		self.combo.current(0)
		self.combo.bind('<<ComboBoxSelected>>')
		self.combo.grid(row=1, column=1)

		self.radio_low.grid(row=1, column=2, sticky=E)
		self.radio_med.grid(row=1, column=3, sticky=E)
		self.radio_high.grid(row=1, column=4, sticky=E)

	def clear(self):
		self.e.delete(0, END)

	def compute(self):

		self.e.delete(0, END)

		length = self.lengthVar.get()
		strength = self.Strength.get()

		lower = 'abcdefghijklmnopqrstuvwxyz'
		upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
		digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()'
		password = ''

		str_choice = ''

		if strength == 1:
			str_choice = lower
		elif strength == 2:
			str_choice = upper
		elif strength == 3:
			str_choice = digits
		else:
			str_choice = lower
		for i in range(length):
			password += random.choice(str_choice)

		return password

	def generate(self):
		pass_ = self.compute()
		self.e.insert(10, pass_)

	def copy(self):
		pass_ = self.e.get()
		pyperclip.copy(pass_)


root = Tk()
root.title(TITLE)
# root.geometry(GEOMETRY)

if RESIZABLE:
	root.resizable(1, 1)
else:
	root.resizable(0, 0)


App = Generator(root)


if __name__ == '__main__':
	root.mainloop()
