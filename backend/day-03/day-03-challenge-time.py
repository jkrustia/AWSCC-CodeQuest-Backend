print("A man knocks on your door and asks for shelter. ")
choice = input("Are you going to let him in? (Type YES or NO)\n")

if choice == "YES":
    print("\nThe police have arrived. They are asking whether the thief is inside.")
    choice = input("What are you going to tell them? (Type YES or NO)\n")

    if choice == "YES":
        print("\nCongratulations! Your smart choices helped the police arrest the criminal.")

    else: 
        print("\nGame over. You got arrested.")

else: 
    print("\nThe man attacked you!")
    choice = input("Will you knock him down? (Type YES or NO)\n")

    if choice == "YES":
        print("\nCongratulations! You successfully defended yourself from the man.")

    else:
        print("\nGame over. You got assaulted.")