import json
import os

def printMenu():
    menu = ("    1 - Add", 
            "    2 - View", 
            "    3 - Search", 
            "    4 - Delete", 
            "    5 - Update",
            "    6 - Exit")
    
    for i in menu:
        print(i)
    

def checkInput(_input):
    global running

    match _input:
        case "1":
            add()

        case "2":
            view()

        case "3":
            websiteName = input("Enter website: ")
            search(websiteName)

        case "4":
            existing = False
            while not existing:
                websiteName = input("Enter website: ")
                existing = isExisting(websiteName)
            delete(websiteName)

        case "5":
            existing = False
            while not existing:
                websiteName = input("Enter website: ")
                existing = isExisting(websiteName)
            update(websiteName)

        case _:
            running = False


def isExisting(websiteName):
    with open("data.json", "r") as file:
        data = json.load(file)
        if websiteName in data:
            return True
        return False


def add():
    print("===========================================")
    print("Add a Password, Email, and Name of Website")
    websiteName = input("\nEnter name of website: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    newData = {
        websiteName: [{
            "email": email,
            "password": password
        }]
    }
    
    with open("data.json", "r") as file:
        data = json.load(file)

    if websiteName in data:
        data[websiteName].append({"email": email, "password": password})
    else:
        data.update(newData)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    os.system("cls")
    print("Successfully added.")


def view():
    os.system("cls")
    with open("data.json", "r") as file:
        data = json.load(file)
        for key, value in data.items():
            print(f"Website: {key}")
            for i in range(len(value)):
                print(f"\tEmail: {value[i]["email"]}")
                print(f"\tPassword: {value[i]["password"]}\n")


def search(websiteName):
    with open("data.json", "r") as file:
        data = json.load(file)
        for key, value in data.items():
            if key == websiteName:
                print(f"Website: {key}")
                for i in range(len(value)):
                    print(f"  {i+1}) Email: {value[i]["email"]}")
                    print(f"\tPassword: {value[i]["password"]}\n")
                return True
        print("Website not found.")
        return False
    

def delete(websiteName):
    with open("data.json", "r") as file:
        data = json.load(file)
        search(websiteName)

        validNum = False
        while not validNum:
            num = int(input("Enter the number that represents the data you want to delete: "))
            validNum = 0 <= (num-1) < len(data[websiteName])

        data[websiteName].pop(num-1)

        if len(data[websiteName]) == 0:
            data.pop(websiteName)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Successfully deleted.")

        
def update(websiteName):
    with open("data.json", "r") as file:
        data = json.load(file)
        search(websiteName)

        validNum = False
        while not validNum:
            num = int(input("Enter the number that represents the data you want to update: "))
            validNum = 0 <= (num-1) < len(data[websiteName])

            toUpdate = input("\"Email\" or \"Password\"").lower()
            newValue = input(f"Enter new {toUpdate}: ")
            data[websiteName][num-1][toUpdate] = newValue

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Successfully updated.")

running = True
while running:
        print("    PASSWORD MANAGER")
        print("========================")
        printMenu()
        userInput = input("\nEnter the number of your chosen function: ")
        checkInput(userInput)

