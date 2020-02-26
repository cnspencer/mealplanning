
import os
import food
import view


def main(ls):
	get = True
	while get:
		print("Add to list options: ")
		print("1. Create new food")
		print("2. Import from another list")
		print("3. Go back")
		op = input()

		if op.isdigit():
			if int(op) == 1:
				name = input("New food name: ")
				nights = input("Leftover nights: ")
				time = input("Prep+Cook time: ")
				ingredients = input("List of ingredients (separate items with \",[SPACE]\"): ").rsplit(", ")
				ls.append(food.Food(name, nights, time, ingredients))
				print(f"{name.title()} added")
			elif int(op) == 2:
				print("Select a list: ")
				count = 1
				lists = []
				for f in os.listdir("../lists"):
					print(f"{count}. {f.replace('.txt', '').title()}")
					count += 1
					lists.append(f)
				listChoice = input()
				if listChoice.isdigit():
					if int(listChoice) < count:
						fname = lists[int(listChoice) - 1]
						file = open("../lists/" + fname, "r")
						list2 = makeFoodList(file, [])
						file.close()
						print(f"{fname.title()} List:")
						view.main(list2)
						print("Name of food to import: ")
						importFood = input()
						for foo in list2:
							if foo.getName().capitalize() is importFood.capitalize():
								ls.append(importFood)
								print(f"{importFood} added")
						else:
							print("Invalid input")
					else:
						print("Invalid input")
				else:
					print("Invalid input")
			elif int(op) == 3:
				get = False
			else:
				print("Invalid input")
		else:
			print("Invalid input")


def makeFoodList(file, ls=None):
	if ls is None:
		ls = []
	for line in file:
		if line is not None:
			line = line.rsplit(":")
			ls.append(food.Food(line[0], nights=line[1], time=line[2], ingredients=line[3]))
	return ls

