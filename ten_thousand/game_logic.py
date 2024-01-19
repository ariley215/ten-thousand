from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        # Initialize score to 0 and create a Counter for counting occurrences of each value
        score = 0
        counts = Counter(dice_roll)

        # Check for a special case where all six dice have different values (1, 2, 3, 4, 5, 6)
        if len(counts) == 6 and all(count == 1 for count in counts.values()):
            score += 1500
            return score

        # Loop through possible dice values (1 to 6) and calculate scores based on the rules
        for value in range(1, 7):
            if value != 1 and value != 5:
                score += value * 100 * (counts[value] // 3)
            elif value == 1:
                score += 1000 * (counts[1] // 3) + 100 * (counts[1] % 3)
            elif value == 5:
                score += 500 * (counts[5] // 3) + 50 * (counts[5] % 3)

        # Check for additional specific conditions and update the score
        score += GameLogic.check_specific_conditions(counts, dice_roll)

       
      

        return score

    @staticmethod
    def check_specific_conditions(counts, dice_roll):
        # Initialize score for specific conditions to 0
        score = 0

        # Loop through counts of each value and apply specific conditions
        for value, count in counts.items():
            if count >= 4:
                score += value * 100
            if count >= 5:
                score += value * 100
            if dice_roll.count(1) == 6:
                score += 1800
            if dice_roll.count(1) == 5:
                score += 1600
            if dice_roll.count(1) == 4:
                score += 800
            if dice_roll.count(5) == 4:
                score -= 50
            if dice_roll.count(5) == 5:
                score -= 100
            if dice_roll.count(2) == 2 and dice_roll.count(3) == 2 and dice_roll.count(6) == 2:
                score += 500

        return score

    @staticmethod
    def roll_dice(num_dice):
        # Generate random values for the specified number of dice (between 1 and 6)
        if 1 <= num_dice <= 6:
            dice_values = tuple(random.randint(1, 6) for _ in range(num_dice))
            return dice_values
        else:
            raise ValueError("Number of dice should be between 1 and 6")
