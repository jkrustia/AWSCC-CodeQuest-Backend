shoppingList = []

while True:
    print("Options:")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")
    
    numOfChoice = int(input("Enter the number of your choice: "))

    if numOfChoice == 1:
        newItem = input("Enter the item you want to add: ")
        shoppingList.append(newItem)
        print(f"{newItem} has been added to your shopping list.\n")

    elif numOfChoice == 2:
        print("Your shopping list:")
        for i in range(len(shoppingList)):
            print(shoppingList[i])
        print("")

    elif numOfChoice == 3:
        deletedItem = input("Enter the item you want to remove: ")
        shoppingList.remove(deletedItem)
        print(f"{deletedItem} has been removed from your shopping list.\n")

    else:
        print("Goodbye!")
        break
