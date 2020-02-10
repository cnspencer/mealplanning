
class Food:
	name = ""
	nights = 0
	time = 0
	ingredients = []

	def __init__(self, name, nights=0, time=0, ingredients=[]):
		self.name = name
		self.nights = nights
		self.time = time
		self.ingredients = ingredients

	def __str__(self):
		return f"{self.name}:" \
			f"Makes {self.nights} dinners" \
			f"Takes {self.time} minutes" \
			f"Uses: {self.ingredients.remove('[', '').remove(']', '')}"

	def getName(self):
		return self.name

	def getNights(self):
		return self.nights

	def getTime(self):
		return self.time

	def getIngredients(self):
		return self.ingredients

	def setName(self, new):
		self.name = new

	def setNights(self, new):
		self.nights = new

	def setTime(self, new):
		self.time = new

	def setIngredients(self, new):
		self.ingredients = new

	def addIngredient(self, ingredient):
		self.ingredients.append(ingredient)

	def removeIngredient(self, ingredient):
		if ingredient in self.ingredients:
			self.ingredients.remove(ingredient)
