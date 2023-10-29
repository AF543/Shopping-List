import sys

# Create the main menu

def mainMenu():
    while True:
        print ()
        print ( ''' ### Shopping List ###

        Select a number for the action that you would like to do:

        1. View shopping list
        2. Add item to shopping list
        3. Check if item is on shopping list
        4. Remove item from shopping list
        5. How many items on shopping list
        6. Clear shopping list
        7. Exit
        ''')

        selection = input ("Enter your selection: ") # Ask the user to enter a selection

        # determine which actions the user makes on the selection below
                    
        if selection == "1":
            showList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            checkItem()
        elif selection == "4":
            removeItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearItem()
        elif selection == "7":
            sys.exit()
        else:
            print("You did not make a valid selection.")
shopping_list = ["tissues", "bread", "jam", "coffee", "bottle water","tomatoes","potatoes"] # Add items to shopping list

# Show all items on the shopping list
def showList ():
    print()
    print("--Shopping List--")
    for i in shopping_list:
        print(" # " + i)

# Add items to the shopping list
def addItem():
    item = input("Enter add item you wish to add to the shopping list: ")
    shopping_list.append(item)
    print(item + " has been added to append shopping list.")

# Check items on the shopping list
def checkItem():
    item = input("What item would like to check on the the shopping list: ")
    if item in shopping_list:
       print("Yes," + item + " is on the shopping list.")
    else:
       print("No," + item + " is not on the shopping list.")

# Remove items from the shopping list
def removeItem():
    item = input("Enter remove item you wish from the shopping list: ")
    shopping_list.remove(item)
    print(item + " has been remove item from the shopping list.")

# How many items are on the shopping list
def listLength():
    print("There are", len(shopping_list), "items on the shopping list.")

# Clear items feom the shopping list
def  clearItem():
    shopping_list.clear()
    print("Shopping list is now cleared.")
    
# Run the function from mainmenu - which will run the app
mainMenu()


