from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        counts = Counter(dice_roll)

        if len(counts) == 6 and all(count == 1 for count in counts.values()):
            score += 1500
            return score

        for value in range(1, 7):
            if value != 1 and value != 5:
                score += value * 100 * (counts[value] // 3)
            elif value == 1:
                score += 1000 * (counts[1] // 3) + 100 * (counts[1] % 3)
            elif value == 5:
                score += 500 * (counts[5] // 3) + 50 * (counts[5] % 3)

        score += GameLogic.check_specific_conditions(counts, dice_roll)

        print("Current score after final:", score)

        return score

    @staticmethod
    def check_specific_conditions(counts, dice_roll):
        score = 0

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
        if 1 <= num_dice <= 6:
            dice_values = tuple(random.randint(1, 6) for _ in range(num_dice))
            return dice_values
        else:
            raise ValueError("Number of dice should be between 1 and 6")

