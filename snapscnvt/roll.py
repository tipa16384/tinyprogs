import random
import sys

def roll_dice(num_dice, num_sides, modifier, discard=None):
    rolls = []

    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)

    # discard the highest or lowest roll
    if discard:
        if discard == 'v':
            rolls.remove(max(rolls))
        elif discard == '^':
            rolls.remove(min(rolls))

    # append modifier to rolls if not zero
    if modifier:
        rolls.append(modifier)

    return sum(rolls), rolls

def parse_arguments(args):
    # rolls is a list of tuples
    # each tuple is (num_dice, num_sides, modifier)
    rolls = []

    for arg in args:
        num_dice = 1
        num_sides = 6
        modifier = None
        discard = None

        # if arg starts with "<n>x" and is followed by a roll specifier, repeat the roll n times
        if 'x' in arg:
            num_repeats, arg = arg.split('x')
            num_repeats = int(num_repeats)
        else:
            num_repeats = 1
        
        # if the arg ends with v or ^, then set discard to that character and remove it from the arg
        if arg.endswith('v') or arg.endswith('^'):
            discard = arg[-1]
            arg = arg[:-1]

        if '+' in arg:
            # capture modifier after the + sign and set arg to the value without the modifier
            arg, modifier = arg.split('+')
        elif '-' in arg:
            # capture modifier after the - sign and set arg to the value without the modifier
            arg, modifier = arg.split('-')
            modifier = -int(modifier)
        if arg.startswith('d'):
            num_sides = int(arg[1:])
        elif 'd' in arg:
            num_dice, num_sides = map(int, arg.split('d'))
        
        for _ in range(num_repeats):
            rolls.append((num_dice, num_sides, int(modifier) if modifier else 0, discard))

    return rolls

def main():
    args = sys.argv[1:]
    trolls = parse_arguments(args)

    for roll in trolls:
        total, rolls = roll_dice(*roll)

        # set arg to a recap of the arguments. Include the modifier if there is one
        arg = f"{roll[0]}d{roll[1]}"
        if roll[2]:
            # handle negative modifier
            if roll[2] < 0:
                arg += f"{roll[2]}"
            else:
                arg += f"+{roll[2]}"

        # if there is a discard, add "discard high" or "discard low" to the arg
        if roll[3]:
            arg += f" discard {roll[3]=='v' and 'high' or 'low'}"

        print(f"{total} = {arg} -> {' + '.join(map(str, rolls))}")

if __name__ == '__main__':
    main()