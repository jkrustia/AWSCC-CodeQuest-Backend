print("Rock, Paper, Scissors... Shoot!")

player1 = input("Player1: ")
player2 = input("Player2: ")

if(player1 == player2):
    print("Tie")
elif(player1 == "Paper" and player2 == "Rock") or (player1 == "Rock" and player2 == "Scissors") or (player1 == "Scissors" and player2 == "Paper"):
    print("\nPlayer1 Wins!")
else:
    print("\nPlayer2 Wins!")