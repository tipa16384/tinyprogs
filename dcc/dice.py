import random

dice_chain = [3,4,5,6,7,8,10,12,14,16,20,24,30]

def improve_die(die: int) -> int:
    """Return the next larger die in the dice chain."""
    try:
        return dice_chain[dice_chain.index(die) + 1]
    except IndexError:
        return die
    
def reduce_die(die: int) -> int:
    """Return the next smaller die in the dice chain."""
    try:
        return dice_chain[dice_chain.index(die) - 1]
    except IndexError:
        return die

def roll_dice(die: int) -> int:
    """Return the result of rolling a die."""
    return random.randint(1, die)

def roll_dice_n_times(die: int, n: int) -> list:
    """Return the results of rolling a die n times."""
    return [roll_dice(die) for _ in range(n)]

def roll_dice_n_times_and_sum(die: int, n: int) -> int:
    """Return the sum of rolling a die n times."""
    return sum(roll_dice_n_times(die, n))
