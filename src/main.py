
import os
import food

"""
This is the base module for a meal planning program.
It is designed to be easily modded by adding your own modules into /src
To create your own module, create a main function that takes a list as an argument. This is the list that the main menu
here asks you to pick. You can add it to the options menu by inputting an option not already listed. It will prompt you 
for a short name for the new option, then where it can find your module from the src/ directory.
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
$"an option name"
>Reference module (path from src/): 
$"x.py"
#TODO: Does it return to the option menu? Guess I'll have to find out.

Then in x.py:
def main(foodsList):
	# your function stuff here


Developed on a Windows 7 machine
@author C. N. Spencer
Maybe a few rights reserved 2020
"""


def main():
	get = True
	file = "../all.txt"
	fname = "../all.txt"
	foods = []
	# This is the main menu
	while get:
		print("Select list: ")
		count = 1
		lists = []
		for f in os.listdir(".."):
			if f.endswith(".txt"):
				print(f"{count}. {f.replace('.txt', '').title()}")
				count += 1
				lists.append(f)
		listChoice = input()
		if listChoice.isdigit():
			if int(listChoice) < count:
				fname = lists[int(listChoice) - 1]
				file = open("../" + fname, "r")
				get = False
		else:
			newChoice = input("Not valid. Create new list?\n")
			if newChoice.capitalize() == "Y" or newChoice.capitalize() == "YES":
				newList = input("Enter list name: ")
				file = open(f"../{newList}.txt", "w+")
				get = False
			else:
				get = True
	foods = makeFoodList(file, foods)
	file.close()

	# This is the option menu
	get = True
	newOption = None
	while get:
		print("Options: ")
		count = 1
		options = []
		f = open("config.txt")
		for op in f:
			if op is not None:
				print(f"{count}. {op}")
				count += 1
				options.append(op)
		print(f"{count}. Exit")

		option = input()
		if option.isdigit():
			if int(option) < count:
				option = int(option)

			elif int(option) == count:  # exit
				get = False
		else:
			option2 = input("Not valid. Create new option?\n")
			if option2.capitalize() == "Y" or option2.capitalize() == "YES":
				newOption = input("Enter option: ")
				module = input("Reference module (path from src/): ").replace(".py", "").replace("/", ".").replace("\\", ".")
		f.close()
		if newOption is not None:
			f = open("config.txt", "a")
			f.write(f"{newOption}:{module}")    # save the new option
			f.flush()
			f.close()

	if option == 1:		# view list option
		printList(foods)
	elif option == 2:   # add food option
		addName = input("New food name: ")
		addNights = input("Leftover nights: ")
		addTime = input("Prep+Cook time: ")
		addIngredients = input("List of ingredients (\",\" regex): ").rsplit(", ")
		foods.append(food.Food(addName, addNights, addTime, addIngredients))
	elif option == 3:   # remove food option
		rmName = input("Name of food to be removed: ")
		foods.remove(rmName)
		# TODO: have it loop back up to the option menu
	else:			    # new option option -- this is wrong: it assumes you want to select the new option you just input
		__import__(module)
		module.main(foods)

	# update list file
	if fname is not "all.txt":
		file = open("../" + fname, "w")
		file.write(writeToFile(foods))
		file.flush()
		file.close()

	# add missing foods to All list
	alltxt = open("../all.txt", "r")
	allFoods = makeFoodList(alltxt)
	alltxt.close()
	for foo in foods:
		if foo not in allFoods:
			allFoods.append(foo)
	alltxt = open("../all.txt", "w")
	alltxt.write(writeToFile(allFoods))
	alltxt.flush()
	alltxt.close()


def makeFoodList(file, ls=[]):
	for line in file:
		if line is not None:
			line = line.rsplit(":")
			ls.append(food.Food(line[0], nights=line[1], time=line[2], ingredients=line[3]))
	return ls


def writeToFile(ls):
	st = ""
	for foo in ls:
		st = st + f"{foo.getName}:{foo.getNights()}:{foo.getTime()}:{foo.getIngredients()}\n"
	return st


def printList(ls):
	for food in ls:
		print(food)


main()
