class Character:

	strength = 10
	dexterity = 10
	intelligence = 10
	stamina = 10

	def __init__(self, name, race, age):
		self.name = name
		self.race = race
		self.age = age

	def printChar(self):
		print("Name: " + self.name)
		print("Race: " + self.race)
		print("Age: " + self.age)

	def setStrength(self, amount):
		self.strength = amount

	def printStrength(self):
		print(self.name + "\'s Strength: " + str(self.strength))