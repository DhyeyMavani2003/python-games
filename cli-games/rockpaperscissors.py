# cli-games/rockpaperscissors.py

# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Rock", "Paper", "Scissors"]

# Generate a random role using an array
computer = roles[randint(0,2)]




boolplayer = False

while boolplayer == False:
    # Get player input
    player = input("Rock, Paper, or Scisors? > ")
    
    # Compare computer and player role
    if computer == player:
      print("DRAW!")
    elif computer == "Rock":
      if player == "Scissors":
        print("You lose!", player, "is destroyed by", computer)
      else:
        print("You win!", player, "covers the", computer)
    elif computer == "Paper":
      if player == "Scissors":
        print("You win!", player, "have cut the", computer)
      else:
        print("You lose!", player, "is covered by", computer)
    elif computer == "Scissors":
      if player == "Paper":
        print("You lose!", player, "is cut by", computer)
      else:
        print("You win!", player, "destroyed the", computer)
    boolplayer = False
    computer = roles[randint(0,2)]

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        boolplayer = False
        computer = roles[randint(0,2)]
    elif play_again == 'no':
        boolplayer = True
        break
