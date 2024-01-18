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
    Prompt the user to enter dice to keep or quit.
    """
    print("Enter dice to keep, or (q)uit:")
    return input("> ").lower()

def end_game(score):
    """
    Display the end game message and the earned points.
    """
    print(f"Thanks for playing. You earned {score} points")

def play_round(round_number, roller=None):
    """
    Play a round of the game.
    """
    start_round(round_number)
    
    print("Rolling 6 dice...")
    current_dice = roll_dice(6)
    display_dice(current_dice)
    
    user_input = user_input_for_keep()

    if user_input == 'q':
        end_game(0)
        return [], []  # Return empty lists when the user quits
    else:
        set_aside, remaining_dice = set_aside_dice(current_dice, user_input)
        
        print("Set Aside:", set_aside)
        print("Remaining Dice:", remaining_dice)
        
        return set_aside, remaining_dice  # Return the values for further use

def play_game():
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
            set_aside, remaining_dice = play_round(round_number)
            total_score += len(set_aside)  # Adjust this based on your scoring logic
            
            # Check if the game continues to the next round or ends
            if not remaining_dice:
                end_game(total_score)
                break

            round_number += 1

if __name__ == '__main__':
    play_game()

    # rolls = [
    #     [],  # Customize this list to control the outcome of rolls
    # ]

    # def mock_roller():
    #     return rolls.pop(0).pop(0)  # pop from the inner list

    # play(roller=mock_roller)
