
import os
import food
import importlib

"""
This is the base module for a meal planning program.
It is designed to be easily modded by adding your own modules into /src
To create your own module, create a main function that takes a list as an argument. You will probably have to import food
as well. This is the list that the main menu here asks you to pick. You can add it to the options menu by inputting an
option not already listed. It will prompt you for a short name for the new option, then where it can find your module
from the src/ directory. See the provided modules (view, add, remove) for example.
i.e.
>Select list: 
>1. list1
>2. list2
>3. list3, etc.
$1
>Options: 
>1. option1
>2. option2
>3. option3, etc.
$aksj3halghs453637ighalgs
>Not valid. Create new option?
$y
>Enter option: 
$an option name
>Reference module (path from src/): 
$x.py

Then in x.py:
def main(foodsList):
	# your function stuff here


Developed on Windows 7/10 machines, Pythons v3.7 and 3.8
@author C. N. Spencer
Maybe a few rights reserved 2020
"""


def main():
	file = mainMenu()
	fname = file.name
	foods = makeFoodList(file, [])
	file.close()
	optionMenu(foods)

	# update list file
	if fname != "all.txt":
		file = open(fname, "w")
		file.write(writeToFile(foods))
		file.flush()
		file.close()

	# add missing foods to All list
	alltxt = open("../lists/all.txt", "r")
	allFoods = makeFoodList(alltxt)
	alltxt.close()
	for foo in foods:
		if foo not in allFoods:
			allFoods.append(foo)
	alltxt = open("../lists/all.txt", "w")
	alltxt.write(writeToFile(allFoods))
	alltxt.flush()
	alltxt.close()


# returns the read-only file (if pre-existing) or newly created file of the list the user picks
def mainMenu():
	get = True
	# This is the main menu
	while get:
		print("Select list (any other key to create new): ")
		count = 1
		lists = []
		for f in os.listdir("../lists"):
			if f.endswith(".txt"):
				print(f"{count}. {f.replace('.txt', '').title()}")
				count += 1
				lists.append(f)
		listChoice = input()
		if listChoice.isdigit():
			if int(listChoice) < count:
				fname = lists[int(listChoice) - 1]
				return open("../lists/" + fname, "r")
			else:
				newChoice = input("Not valid. Create new list?\n")
				if newChoice.capitalize() == "Y" or newChoice.capitalize() == "YES":
					newList = input("Enter list name: ")
					return open(f"../lists/{newList}.txt", "w+")
				else:
					get = True
		else:
			newChoice = input("Not valid. Create new list (y/n)?\n")
			if newChoice.capitalize() == "Y" or newChoice.capitalize() == "YES":
				newList = input("Enter list name: ")
				return open(f"../lists/{newList}.txt", "w+")
			else:
				get = True


def optionMenu(foods):
	# This is the option menu
	get = True
	newOption = None
	while get:
		print("Options (any other key to create new): ")
		count = 1
		options = []
		f = open("config.txt")
		for op in f:
			if op is not None:
				opName = op.rsplit(':')[0].replace('\n', '')
				opMod = op.rsplit(":")[1].replace("\n", "")
				print(f"{count}. {opName}")
				count += 1
				options.append(f"{opName}:{opMod}")
		print(f"{count}. Exit")

		option = input()
		if option.isdigit():
			if int(option) < count:
				opMod = options[int(option) - 1].rsplit(":")[1]
				try:
					mod = importlib.import_module(opMod)  # imports and executes your module option
					mod.main(foods)
				except ModuleNotFoundError:
					print("Error: No module was found at " + opMod + " for option " + option)
					print("See if src/config.txt is correctly configured (ex. \"My Option:mymod\")")
			elif int(option) == count:  # exit
				get = False
		else:
			optionMake = input("Not valid. Create new option?\n")
			if optionMake.capitalize() == "Y" or optionMake.capitalize() == "YES":
				newOption = input("Enter option: ")
				module = input("Reference module (path from src/): ").replace(".py", "").replace("/", ".").replace("\\", ".")
		f.close()
		if newOption is not None:
			f = open("config.txt", "a")
			f.write(f"\n{newOption}:{module}")  # save the new option
			f.flush()
			f.close()


def makeFoodList(file, ls=None):
	if ls is None:
		ls = []
	for line in file:
		if line is not None:
			line = line.rsplit(":")
			ls.append(food.Food(line[0], nights=line[1], time=line[2], ingredients=line[3]))
	return ls


def writeToFile(ls):
	st = ""
	for foo in ls:
		st = st + f"{foo.getName()}:{foo.getNights()}:{foo.getTime()}:{foo.getIngredients()}\n"
	return st


main()
