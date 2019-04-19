import tkinter as tk
from tkinter import messagebox


import Character


"""
This class is the root GUI that displays the starting screen
"""
class StartScreen(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.oarent = parent

		#add remaining elements here

if __name__ == "__main__":
	root = tk.Tk()
	StartScreen(root).pack(side="top", fill="both", expand=True)
	root.mainloop()