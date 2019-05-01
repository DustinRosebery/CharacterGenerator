import tkinter as tk
import Character as c
 
"""
This class is the root GUI that displays the starting screen
"""
class StartScreen(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		createButton = tk.Button(self, text="Create", 
			command=lambda: self.createCharacter("Duster Scruggs", "Dustin", "100"))
		createButton.place(x=20, y=20)
		self.pack(side="top", fill="both", expand=True)

		#add remaining elements here

	def createCharacter(self, name, player, points):
		character = c.Character(name, player, points)
		character.updateAttribute("ST", 3)
		character.updateAttribute("DX", 2)
		character.updateAttribute("IQ", -2)
		character.updateAttribute("WILL", 5)
		character.updateAttribute("BS", 3)
		character.updateAttribute("BM", 2)
		character.addNewAdvantage("360_degree_vision")
		character.printCharacter()

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("300x300+300+300")
	StartScreen(root).pack(side="top", fill="both", expand=True)
	root.mainloop()