import random

print("Rock, Paper, Scissors...")

options = ["Rock", "Paper", "Scissors"]

playerChoice = input("Shoot! ----> ").lower()
computerChoice = random.choice(options).lower()

print(f"\n{playerChoice.upper()} VS {computerChoice.upper()}\n")

if(playerChoice == computerChoice):
    print("It's a draw.")

elif(playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "paper" and computerChoice == "rock") or (playerChoice == "scissors" and computerChoice == "paper"):
    print("You win!")

else:
    print("You lose.")