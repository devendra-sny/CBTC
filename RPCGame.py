import random

options = ("rock", "paper", "scissor")
playing = True

print('Winning Rules as follows:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ")

    print("Player: ", player)
    print("Computer: ", computer)

    if player == computer:
        print("It's a tie game!")
    elif player == "rock" and computer == "scissor":
        print("Rock wins")
    elif player == "paper" and computer == "rock":
        print("Paper wins")
    elif player == "scissor" and computer == "paper":
        print("Scissor wins")
    else:
        print("You lose!")

    Play_Again = input("Play again? (y/n): ").lower()
    if not Play_Again == "y":
        playing = False

print("Thanks for playing Rock Paper Scissor Game!")
