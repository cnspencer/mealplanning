"""
A food object requires a name, a number of leftover nights, cook and prep time, and a list of ingredients
Additional object data fields can be added dynamically within mods as long as these four are first in order when saved to the list file

@author C. N. Spencer
"""


class Food:
	name = ""
	nights = 0
	time = 0
	ingredients = []

	def __init__(self, name, nights=0, time=0, ingredients=None):
		self.name = name
		self.nights = nights
		self.time = time
		if ingredients is not None:
			self.ingredients = ingredients
		else:
			self.ingredients = []

	def __str__(self):
		return str(self.name) + ":\nMakes " + str(self.nights) + " leftover nights\nTakes " + str(self.time) + " minutes to make\nUses " + str(self.ingredients).replace('[', '').replace(']', '')

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
