import Advantages
import Attributes

class Character:

	def __init__(self, name, player, points):
		self.name = name
		self.player = player
		self.totalPoints = points
		self.unspentPoints = points
		self.spentPoints = 0

		self.attributes = Attributes.Attributes()
		self.advantages = []

	# Updates 1 of:
	#     Primary Attribute ST, DX, IQ, HT -or-
	#     Tertiary Attribute HP, WILL, PER, FP -or-
	#     Secondary Characteristic BS, BM
	# for primary attributes, this will also update the corresponding tertiary attributes
	def updateAttribute(self, attribute, amount):
		if(attribute == "ST"):
			cost = self.attributes.setStrength(amount)
		elif(attribute == "DX"):
			cost = self.attributes.setDexterity(amount)
		elif(attribute == "IQ"):
			cost = self.attributes.setIntelligence(amount)
		elif(attribute == "HT"):
			cost = self.attributes.setHealth(amount)
		elif(attribute == "HP"):
			cost = self.attributes.setHeatlhPoints(amount)
		elif(attribute == "WILL"):
			cost = self.attributes.setWill(amount)
		elif(attribute == "PER"):
			cost = self.attributes.setPerception(amount)
		elif(attribute == "FP"):
			cost = self.attributes.setFatiguePoints(amount)
		elif(attribute == "BS"):
			cost = self.attributes.setBasicSpeed(amount)
		elif(attribute == "BM"):
			cost = self.attributes.setBasicMove(amount)
		else:
			cost = 0
			print("Unable to update " + attribute)
			print("Please enter one of: ST, DX, IQ, HT, HP, WILL, PER, FP, BS, or BM")
		self.unspentPoints = int(self.unspentPoints) - cost
		self.spentPoints = int(self.spentPoints) + cost
		self.attributes.updateTertiaryAttributes()

	def addNewAdvantage(self, name):
		self.advantages.append(Advantages.add(name)) 

	def printCharacter(self):
		print("********CHARACTER SHEET********")
		print("Name:\t\t\t" + str(self.name))
		print("Player:\t\t\t" + str(self.player))
		print("Total Points:\t" + str(self.totalPoints))
		print("Spent Points:\t" + str(self.spentPoints))
		print("Unspent Points:\t" + str(self.unspentPoints))
		print("\nPRIMARY ATTRIBUTES")
		print("\tST:\t\t\t" + str(self.attributes.getStrength()))
		print("\tST cost:\t" + str(self.attributes.stSpentPoints))
		print("\tDX:\t\t\t" + str(self.attributes.getDexterity()))
		print("\tDX cost:\t" + str(self.attributes.dxSpentPoints))
		print("\tIQ:\t\t\t" + str(self.attributes.getIntelligence()))
		print("\tIQ cost:\t" + str(self.attributes.iqSpentPoints))
		print("\tHT:\t\t\t" + str(self.attributes.getHealth()))
		print("\tHT cost:\t" + str(self.attributes.htSpentPoints))
		print("\nTERTIARY ATTRIBUTES")
		print("\tHP:\t\t\t" + str(self.attributes.getHitPoints()))
		print("\tHP cost:\t" + str(self.attributes.hpSpentPoints))
		print("\tWILL:\t\t" + str(self.attributes.getWill()))
		print("\tWILL cost:\t" + str(self.attributes.willSpentPoints))
		print("\tPER:\t\t" + str(self.attributes.getPerception()))
		print("\tPER cost:\t" + str(self.attributes.perSpentPoints))
		print("\tFP:\t\t\t" + str(self.attributes.getFatiguePoints()))
		print("\tFP cost:\t" + str(self.attributes.fpSpentPoints))
		print("\nSECONDARY CHARACTERISTICS")
		print("\tThrust:\t\t\t" + str(self.attributes.getThrust()))
		print("\tSwing:\t\t\t" + str(self.attributes.getSwing()))
		print("\tBasic Speed:\t" + str(self.attributes.getBasicSpeed()))
		print("\tBS cost:\t\t" + str(self.attributes.bsSpentPoints))
		print("\tBasic Move:\t\t" + str(self.attributes.getBasicMove()))
		print("\tBM cost:\t\t" + str(self.attributes.bmSpentPoints))
		print("")
