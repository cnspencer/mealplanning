
# mealplanning
A modular program by C. N. Spencer

The purpose of the mealplanning program is to help plan dinners (or any meals you need, really) by creating lists of foods you would like to make.

# To Start mealplanning
You can run it by double clicking src/main.py or from the commandline with the following command from the mealplanning/ folder (you may find that the "3" on python is unnecessary if you have no other versions installed):

    python3 src/main.py main
    
# Base Mods
Mealplanning, though designed to be a modular program for easy community modding, includes some basic functionality for the simpletons or indolent of us who would rather not have to make up our own programs. The following come standard with mealplanning and are ready to use out-of-the-box:
* View
	* Prints the current list to the console
* Add
	* Adds an existing or new food to the current list
* Remove
	* Removes a specified food from the current list

# TODO list:
Add some more basic modules like shufflePlan, findQuick, etc.

Refactor food.py to allow for new data fields (see TODO in food.py)

Eventually migrate to Java to create JavaFX GUI

# Future Mods:
shufflePlan: takes the list and plans out your meals randomly

findQuick: finds the three quickest meals to make

findBalanced: finds the most balanced meal according to cook/prep time, leftover nights, and number of ingredients
