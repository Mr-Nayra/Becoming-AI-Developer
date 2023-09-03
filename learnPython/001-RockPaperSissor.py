import random

def get_choices():
    player_choice = input("Enter a choice (rock/paper/scissors) ")
    options = ["paper", "rock", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if(player == computer):
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You won"
    
    return "computer won"
    
choices = get_choices()
print(check_win(choices["player"], choices["computer"]))

