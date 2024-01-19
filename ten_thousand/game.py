import random
import sys
from ten_thousand.game_logic import GameLogic

def welcome_prompt():
    """
    Display the welcome message and prompt the user to play or decline.
    """
    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
    user_input = input("> ")
    return user_input.lower()

def start_round(round_number):
    """
    Display the start of a new round message.
    """
    print(f"Starting round {round_number}")

def roll_dice(roller):
    """
    Roll a specified number of dice using GameLogic and return the results.
    """
    return GameLogic.roll_dice(roller)

def display_dice(dice_results):
    """
    Display the rolled dice results.
    """
    print("***", " ".join(map(str, dice_results)), "***")

def user_input_for_keep():
    """
    Prompt the user to enter dice to keep, or quit.
    """
    print("Enter dice to keep, or (q)uit:")
    return input("> ").lower()
  
def handle_dice_to_keep(user_input):
    """
    Handle the user input for dice to keep.
    """
    # Split the input string by character and convert to integers
    dice_to_keep = [int(char) for char in user_input if char.isdigit()]

    return dice_to_keep

def end_game(score):
    """
    Display the end game message and the earned points.
    """
    print(f"Thanks for playing. You earned {score} points")

def set_aside_dice(dice_results, dice_to_keep):
    """
    Set aside the dice with the specified values.
    """
    set_aside = [die for die in dice_results if die in dice_to_keep]
    remaining_dice = [die for die in dice_results if die not in dice_to_keep]
    return set_aside, remaining_dice

def play_round(round_number, total_score):
    """
    Play a round of the game.
    """
    start_round(round_number)
    
    print(f"Rolling 6 dice... Total Score: {total_score}")
    current_dice = roll_dice(6)
    display_dice(current_dice)
    
    user_input = user_input_for_keep()

    if user_input == 'q':
        end_game(total_score)
        sys.exit()
    else:
        dice_to_keep = handle_dice_to_keep(user_input)
        set_aside, remaining_dice = set_aside_dice(current_dice, dice_to_keep)
        
        print(f"You have {total_score} unbanked points and {len(remaining_dice)} dice remaining")
        action = input("(r)oll again, (b)ank your points or (q)uit:\n> ").lower()

        if action == 'r':
            return remaining_dice, total_score
        elif action == 'b':
            round_score = GameLogic.calculate_score(set_aside)
            total_score += round_score
            print(f"You banked {round_score} points in round {round_number}")
            print(f"Total score is {total_score} points")
            return roll_dice(6), total_score
        elif action == 'q':
            end_game(total_score)
            sys.exit()

def play():
    """
    Play the entire game, including multiple rounds.
    """
    user_response = welcome_prompt()

    if user_response == 'n':
        print('OK. Maybe another time')
        sys.exit()
    elif user_response == 'y':
        round_number = 1
        total_score = 0

        while True:
            remaining_dice, total_score = play_round(round_number, total_score)
            
            if not remaining_dice:
                end_game(total_score)
                sys.exit()

            round_number += 1

if __name__ == '__main__':
    play()



    # rolls = [
    #     [],  # Customize this list to control the outcome of rolls
    # ]

    # def mock_roller():
    #     return rolls.pop(0).pop(0)  # pop from the inner list

    # play(roller=mock_roller)
