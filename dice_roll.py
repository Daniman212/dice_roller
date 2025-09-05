import random

def roll_dice(num_dice, sides=6):
    """Roll num_dice dice with the given number of sides."""
    return [random.randint(1, sides) for _ in range(num_dice)]