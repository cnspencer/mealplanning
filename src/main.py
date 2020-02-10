
import os
import food

"""
This is the basic module for a meal planning program.
It is designed to be easily modded by adding your own modules into /src
To create your own module, create a main function that takes a list as an argument. This is the list that the main menu
first asks you to pick. You can add it to the options menu by inputting an option not already listed. It will prompt you 
for a short name for the new option, then where it can find your module.


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
				file = open(fname, "r")
				get = False
		else:
			newChoice = input("Not valid. Create new list?\n")
			if newChoice.capitalize() == "Y" or newChoice.capitalize() == "YES":
				newList = input("Enter list name: ")
				file = open(f"../{newList}", "w+")
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
		for line in f:
			print(f"{count}. {line}")
			count += 1
			options.append(line)
		option = input()
		if option.isdigit():
			if int(option) < count:
				option = int(option)
				get = False
		else:
			option2 = input("Not valid. Create new option?\n")
			if option2.capitalize() == "Y" or option2.capitalize() == "YES":
				newOption = input("Enter option: ")
				module = input("Reference module (path from src/): ").replace(".py", "")
		f.close()
		if newOption is not None:
			f = open("config.txt", "a")
			f.write(f"{newOption}:{module}")
			f.flush()
			f.close()

	if option == 1:
		printList(foods)
	elif option == 2:
		addName = input("New food name: ")
		addNights = input("Leftover nights: ")
		addTime = input("Prep+Cook time: ")
		addIngredients = input("List of ingredients (\",\" regex): ").rsplit(", ")
		foods.append(food.Food(addName, addNights, addTime, addIngredients))
	elif option == 3:
		rmName = input("Name of food to be removed: ")
		foods.remove(rmName)
	else:
		__import__(module)
		module.main(foods)

	file = open(fname, "w")
	file.write(writeToFile(foods))
	file.flush()
	file.close()


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
