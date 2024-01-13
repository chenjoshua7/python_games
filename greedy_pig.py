##                       ##
##    Greedy Pig Game    ##
##                       ##
###########################

# The greedy pig game is a game that I played with my students when I taught them probability.
#
# The rules of the game are very simple. You roll keep rolling a dice. Whatever number you get
# is added to your score. However, if you roll a 1, your score drops to 0. You can play the 
# game with multiple people and play multiple rounds. Winner is who has the most points at the
# end of all the round.
#
# This was coded from scratch without any tutorials

import random

round_score = 0
continue_game = True
turn_count = 0

player_score = []
round_score = 0
round_count = 1

def roll_dice():
    global round_score, continue_game
    roll = random.randint(1, 6)
    
    if roll == 1:
        round_score = 0
        print("Rolled a 1. You lose all your points.")
        continue_game = False
    else:
        round_score += roll
        print(f"You rolled a {roll}")
        print(f"Your score is now: {round_score}")

def get_user_input():
    while True:
        try:
            user_input = input('Enter 1 if you want to roll again: ')
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def playRound():
    global continue_game, turn_count, round_score, player_score, round_count
    print(f"Round {round_count}:")
    while continue_game:
        turn_count += 1
        roll_dice()
        if continue_game:
            continue_game = get_user_input()
    print(f"Your score for Round {round_count} was {round_score}")
    print(f"You rolled {turn_count} time(s)")
    pause()
    player_score.append(round_score)
    round_count += 1
    
def resetRound():
    global round_score, turn_count, continue_game
    round_score = 0
    continue_game = True
    turn_count = 0
    
def playGame():
    global round_count, final_score
    while round_count <= 5:
        resetRound()
        playRound()
    final_score = sum(player_score)
    print(f"Your final score after 5 rounds is {final_score}")

def pause():
    Pause = input("Press the <ENTER> key to continue to the next round...")

playGame()