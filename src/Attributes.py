import AttributeTables as aT

"""
	This Class contains all primary and tertiary attributes and point costs
"""
class Attributes:

	def __init__(self):
		# primary attributes
		self.strength = 10
		self.dexterity = 10
		self.intelligence = 10
		self.health = 10
		# primary attribute cost
		self.stCost = 10
		self.dxCost = 20
		self.iqCost = 20
		self.htCost = 10
		#primary attribute spent points
		self.stSpentPoints = 0
		self.dxSpentPoints = 0
		self.iqSpentPoints = 0
		self.htSpentPoints = 0

		# tertiary attributes
		self.hitPoints = self.strength
		self.will = self.intelligence
		self.perception = self.intelligence
		self.fatiguePoints = self.health
		# tertiary attribute bonuses
		self.hpBonusAmount = 0
		self.willBonusAmount = 0
		self.perBonusAmount = 0
		self.fpBonusAmount = 0
		# tertiary attribute cost
		self.hpCost = 2
		self.willCost = 5
		self.perCost = 5
		self.fpCost = 3
		# tertiary attribute spent points
		self.hpSpentPoints = 0
		self.willSpentPoints = 0
		self.perSpentPoints = 0
		self.fpSpentPoints = 0

		# secondary characteristics
		self.damage = aT.damageTable[self.strength].split(" ")
		self.thrust = self.damage[0]
		self.swing = self.damage[1]
		self.basicSpeed = (self.health + self.dexterity) / 4
		self.basicMove = self.basicSpeed / 1
		self.encumberance = 0
		self.basicLift = aT.encumberanceTable[self.strength][0]
		# secondary characteristic bonuses
		self.basicSpeedBonusAmount = 0
		self.basicMoveBonusAmount = 0
		# secondary characteristic cost
		self.bsCost = 5
		self.bmCost = 5
		# secondary characteristic spent points
		self.bsSpentPoints = 0
		self.bmSpentPoints = 0 
		# secondary characteristic modifier
		self.basicSpeedBonusModifier = 0.25


	# primary attribute getters and setters
	# All setters return the point cost of the the operation
	def setStrength(self, amount):
		cost = int(amount * self.stCost)
		self.strength += amount
		self.stSpentPoints += cost
		return(cost)

	def getStrength(self):
		return self.strength

	def setDexterity(self, amount):
		cost = int(amount * self.dxCost)
		self.dexterity += amount
		self.dxSpentPoints += cost
		return(cost)

	def getDexterity(self):
		return self.dexterity

	def setIntelligence(self, amount):
		cost = int(amount * self.iqCost)
		self.intelligence += amount
		self.iqSpentPoints += cost
		return(cost)

	def getIntelligence(self):
		return self.intelligence

	def setHealth(self, amount):
		cost = int(amount * self.htCost)
		self.health += amount
		self.htSpentPoints += cost
		return(cost)

	def getHealth(self):
		return self.health

	# tertiary attribute getters and setters
	# All setters return the point cost of the operation
	def setHitPoints(self, amount):
		cost = int(amount * self.hpCost)
		self.hpBonusAmount += amount
		self.hpSpentPoints += cost
		return(cost)

	def getHitPoints(self):
		return self.hitPoints

	def setWill(self, amount):
		cost = int(amount * self.willCost)
		self.willBonusAmount += amount
		self.willSpentPoints += cost
		return(cost)

	def getWill(self):
		return self.will

	def setPerception(self, amount):
		cost = int(amount * self.perCost)
		self.perBonusAmount += amount
		self.perSpentPoints += cost
		return(cost)

	def getPerception(self):
		return self.perception

	def setFatiguePoints(self, amount):
		cost = int(amount * self.fpCost)
		self.fpBonusAmount += amount
		self.dxSpentPoints += cost
		return(cost)

	def getFatiguePoints(self):
		return self.fatiguePoints

	# secondary characteristic getters and setters
	# All setters return the point cost of the operation
	def getThrust(self):
		return self.thrust

	def getSwing(self):
		return self.swing

	def setBasicSpeed(self, amount):
		cost = int(amount * self.bsCost)
		self.basicSpeedBonusAmount += amount
		self.bsSpentPoints += cost
		return (cost)

	def getBasicSpeed(self):
		return self.basicSpeed

	def setBasicMove(self, amount):
		cost = int(amount * self.bmCost)
		self.basicMoveBonusAmount += amount
		self.bmSpentPoints += cost
		return(cost)

	def getBasicMove(self):
		return self.basicMove

	# updates all tertiary attributes and secondary characteristics
	# based on primary attributes and bonuses
	def updateTertiaryAttributes(self):
		self.hitPoints = self.strength + self.hpBonusAmount
		self.will = self.intelligence + self.willBonusAmount
		self.perception = self.intelligence + self.perBonusAmount
		self.fatiguePoints = self.health + self.fpBonusAmount
		self.damage = aT.damageTable[self.strength].split(" ")
		self.thrust = self.damage[0]
		self.swing = self.damage[1]
		self.basicSpeed = (self.health + self.dexterity) / 4 + (self.basicSpeedBonusModifier * self.basicSpeedBonusAmount)
		self.basicMove = int(self.basicSpeed / 1) + self.basicMoveBonusAmount