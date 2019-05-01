class Advantages:

	advantages = {
		"360_degree_vision" : {
			"name" : "360 Degree Vision",
			"baseCost" : 25,
			"description" : "You have a 360* field of vision. You have NO penalty to defend against attacks from the sides or rear. You can attack foes to your sides or rear without making a Wild Swing, but you are at -2 to hit due to the clumsy angle of attack (note that some Karate techniques do NOT suffer this penalty). Finally, you are at +5 to detect Shadowing attempts, and are never surprised by a danger that comes from behind, unless it also is concealed from sight. Extra eyes are merely a special effect of this trait - you can have any number of eyes, but the cost remains the same",
			"enhancements" : [],
			"limitations" : ["Easy to Hit", "Your eyes are on stalks, unusually large, or otherwise more vulnerable to attack. Others can target your eyes from within their arc of vision at only -6 to hit", -0.2],
			"hasLevels" : False,
			"amount" : 1
		},
		"absolute_direction" : {
			"name" : "",
			"baseCost" : 5,
			"description" : "",
			"enhancements" : [],
			"limitations" : [],
			"hasLevels" : False,
			"amount" : 1
		}
	}

	def __init__(self, name, baseCost, description, enhancements, limitations, hasLevels, amount):
		self.name = name
		self.baseCost = baseCost
		self.description = description
		self.enhancements = enhancements
		self.limitations = limitations
		self.hasLevels = hasLevels
		self.amount = amount


	@classmethod
	def add(cls, name):
		item = advantages[name]
		if(item):
			return(Advantages(item["name"], item["baseCost"], item["description"], item["enhancements"], item["limitations"], item["hasLevels"], item["amount"]))
		else:
			print("Advantage not found: " + name)
			return()



