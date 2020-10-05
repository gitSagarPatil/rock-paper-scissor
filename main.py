from random import randint

# create a list of play options
comp_select = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = comp_select[randint(0, 2)]

# set player and computer win count
player_won = 0
computer_won = 0

# set number of games
n = int(input("How many games you want to play? "))

for i in range(0, n):
    # set player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_won += 1
        else:
            print("You win!", player, "smashes", computer)
            player_won += 1

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computer_won += 1
        else:
            print("You win!", player, "covers", computer)
            player_won += 1

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computer_won += 1
        else:
            print("You win!", player, "cut", computer)
            player_won += 1
    else:
        print("That's not a valid play. Check your spelling!")

    computer = comp_select[randint(0, 2)]

if computer_won > player_won:
    print("Computer Won!!")
    print("Computer Score -> ",computer_won)
    print("Player Score -> ", player_won)

elif computer_won < player_won:
    print("Player Won!!")
    print("Computer Score -> ", computer_won)
    print("Player Score -> ", player_won)

else:
    print("It is a tie!!")
    print("Computer Score -> ", computer_won)
    print("Player Score -> ", player_won)
