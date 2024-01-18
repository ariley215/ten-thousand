import random
import sys

def play(roller=None):
    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
    user_input = input("> ")
    if user_input.lower() == 'n':
      print('OK. Maybe another time')
      sys.exit() 
    if user_input.lower() == 'y':
        print("Starting round 1")
        print("Rolling 6 dice...")  # Modified to match the expected output
        current_dice = roll_dice(6)
        print("***", " ".join(map(str, current_dice)), "***")
        

        print("Enter dice to keep, or (q)uit:")
        user_input = input("> ")

        if user_input.lower() == 'q':
            print("Thanks for playing. You earned 0 points")
            return [], []  # Return empty lists when the user quits
        else:
            
            # Handle the user's input for keeping dice and continue the game
            # Adjust this part based on your actual game logic
            set_aside, remaining_dice = set_aside_dice(current_dice, user_input)
            
            print("Set Aside:", set_aside)
            print("Remaining Dice:", remaining_dice)
            
            return set_aside, remaining_dice  # Return the values for further use

 # use GameLogic to bank 

def roll_dice(roller):
    """
    Roll a specified number of dice and return the results.
    """
    return [random.randint(1, 6) for _ in range(roller)]

def set_aside_dice(dice_results, set_aside_values):
    """
    Set aside the dice with the specified values.
    """
    set_aside_values = set(map(int, set_aside_values.split()))
    return [die for i, die in enumerate(dice_results) if i in set_aside_values], \
           [die for i, die in enumerate(dice_results) if i not in set_aside_values]

# Example usage:
# set_aside, remaining_dice = play(6)
# print("Set Aside:", set_aside)y

# print("Remaining Dice:", remaining_dice)
play()
