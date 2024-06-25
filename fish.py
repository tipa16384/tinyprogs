import curses
import random
import time

# Constants for the screen size
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24

# Fish movement constraints
MAX_VERTICAL_VELOCITY = 1

# Probability constants for changing velocity
CHANGE_VELOCITY_PROB = 0.05

# probability fish dies
DIE_PROB = 0.02

# probability fish reproduces
REPRODUCE_PROB = 0.022

# probability substrate destroyed
DESTROY_PROB = DIE_PROB * 4

class Species:
    color_pair_number = 2

    def __init__(self, image: str, color: int = curses.COLOR_WHITE):
        self.image = image
        self.last_image = image
        # flipped image is reversed image, but with < -> >, > -> <, ( -> ), ) -> (
        self.flipped_image = image[::-1].replace("<", " ").replace(">", "<").replace(" ", ">").replace("(", " ").replace(")", "(").replace(" ", ")")
        self.color = color
        curses.init_pair(Species.color_pair_number, color, -1)
        self.color_pair_number = Species.color_pair_number
        Species.color_pair_number += 1

    def get_image(self, dx: float) -> str:
        "if dx > 0, return the image, if dx = 0, return last image, if dx < 0 return the flipped image, update last_image"
        if dx > 0:
            self.last_image = self.image
            return self.image
        elif dx == 0:
            return self.last_image
        else:
            self.last_image = self.flipped_image
            return self.flipped_image
    
    def __len__(self) -> int:
        return len(self.image)

class Fish:
    def __init__(self, species: Species, x: float, y: float, vx: float, vy: float):
        self.species = species
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def update(self, substrate):
        tx = self.x + self.vx
        ty = self.y + self.vy

        # Change velocity infrequently
        if random.random() < CHANGE_VELOCITY_PROB:
            self.vx = (random.random() - 0.5) * len(self.species)
            self.vy = (random.random() - 0.5) * MAX_VERTICAL_VELOCITY

        # Ensure the fish stays within screen boundaries
        if tx < 0:
            tx = 0
            self.vx = abs(self.vx)
        elif tx > SCREEN_WIDTH - len(self.species):
            tx = SCREEN_WIDTH - len(self.species)
            self.vx = -abs(self.vx)

        if ty < 0:
            ty = 0
            self.vy = abs(self.vy)
        elif ty > SCREEN_HEIGHT - 1:
            ty = SCREEN_HEIGHT - 1
            self.vy = -abs(self.vy)
        
        # update the position of the fish only if no substrate is present at the new position along the length of the fish
        if all([(round(ty), round(tx + i)) not in substrate for i in range(len(self.species))]):
            self.x = tx
            self.y = ty
        else:
            self.vy -= 0.5


def main(stdscr):
    global SCREEN_WIDTH, SCREEN_HEIGHT
    curses.start_color()
    curses.use_default_colors()
    # color pair 1 is gray
    curses.init_pair(1, curses.COLOR_YELLOW, -1)

    SCREEN_HEIGHT, SCREEN_WIDTH = stdscr.getmaxyx()
    print (f"Screen height: {SCREEN_HEIGHT}, Screen width: {SCREEN_WIDTH}")

    basic_fish = Species("><(((>", curses.COLOR_MAGENTA)
    small_fish = Species("><>", curses.COLOR_RED)
    medium_fish = Species("><>>", curses.COLOR_BLUE)
    long_fish = Species("><((()))>", curses.COLOR_GREEN)
    species = [basic_fish, small_fish, medium_fish, long_fish]

    fishes = [Fish(random.choice(species), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, random.choice([-1, 1]), random.choice([-1, 0, 1])) for _ in range(10)]

    # Turn off cursor blinking
    curses.curs_set(0)
    
    # Set up the screen
    stdscr.nodelay(1)
    stdscr.timeout(100)

    substrate = define_substrate((SCREEN_HEIGHT * SCREEN_WIDTH) // 10)

    while True:
        # Draw the fish
        stdscr.clear()

        render_substrate(stdscr, substrate)

        for fish in fishes:
            x = fish.x
            y = fish.y
            vx = fish.vx

            image = fish.species.get_image(vx)
            stdscr.addstr(round(y), round(x), image, curses.color_pair(fish.species.color_pair_number))

        stdscr.refresh()

        # Handle key press to exit
        key = stdscr.getch()
        if key != -1:
            break

        # Update the fish position
        for fish in fishes:
            fish.update(substrate)
        
        # if random < DIE_PROB, remove a fish
        if random.random() < DIE_PROB:
            dead_fish = fishes.pop(random.randint(0, len(fishes) - 1))
            # create substrate at the length and position of the dead fish
            for i in range(len(dead_fish.species)):
                substrate.append((round(dead_fish.y), round(dead_fish.x + i)))

        # Reproduce fish
        if random.random() < REPRODUCE_PROB:
            parent = random.choice(fishes)
            parent_species = parent.species
            # 50% chance that the child is a random species
            if random.random() < 0.5:
                child_species = random.choice(species)
            else:
                child_species = parent_species
            child = Fish(child_species, parent.x, parent.y, parent.vx, parent.vy)
            fishes.append(child)
        
        substrate = move_substrates(substrate)
        substrate = delete_last_substrate(substrate)

        time.sleep(0.1)

def delete_last_substrate(substrate: list) -> list:
    "if random < DESTROY_PROB, delete a random substrate from the list"
    if random.random() < DESTROY_PROB:
        substrate.pop(random.randint(0, len(substrate) - 1))

    return substrate

def move_substrates(substrate: list):
    "move the substrate down by 1"
    # for each element of substrate, remove it from the list, see if it can be moved down by 1, if it can, add it back to the list
    new_substrate = []
    while substrate:
        total_substrate = substrate + new_substrate
        y, x = substrate.pop()
        if y < SCREEN_HEIGHT - 1:
            left_free = x > 0 and (y+1, x - 1) not in total_substrate
            right_free = x < SCREEN_WIDTH - 1 and (y+1, x + 1) not in total_substrate
            down_free = (y + 1, x) not in total_substrate
            if down_free:
                y += 1
            elif left_free and right_free:
                x += random.choice([-1, 1])
                y += 1
            elif left_free:
                x -= 1
                y += 1
            elif right_free:
                x += 1
                y += 1

        new_substrate.append((y, x))

    return new_substrate

def define_substrate(zoop) -> list:
    substrate = []
    for _ in range(zoop):
        y, x = 0, random.randint(0, SCREEN_WIDTH - 1)
        stopped = False
        while not stopped:
            if y >= SCREEN_HEIGHT - 1:
                stopped = True
            else:
                left_free = x > 0 and (y+1, x - 1) not in substrate
                right_free = x < SCREEN_WIDTH - 1 and (y+1, x + 1) not in substrate
                down_free = (y + 1, x) not in substrate
                if down_free:
                    y += 1
                elif left_free and right_free:
                    x += random.choice([-1, 1])
                    y += 1
                elif left_free:
                    x -= 1
                    y += 1
                elif right_free:
                    x += 1
                    y += 1
                else:
                    stopped = True

        substrate.append((y, x))

    return substrate

        

def render_substrate(stdscr, substrate: list):
    for y, x in substrate:
        try:
            stdscr.addch(y, x, "o", curses.color_pair(1))
        except curses.error:
            pass

curses.wrapper(main)
