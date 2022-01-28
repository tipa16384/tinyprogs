import base64
from pygame.image import load
import pygame
import heapq
from functools import lru_cache, reduce
import sys

header = 'data:image/png;base64,'
bits = 0
graphics = False

def compress(rows: list) -> int:
    compressed = 0
    cell_count = 0
    for row in rows:
        for pixel in row:
            if pixel == True:
                compressed = compressed << 1 | 1
                cell_count += 1
            elif pixel == False:
                compressed = compressed << 1
                cell_count += 1
    return compressed


def uncompress(template: list, compressed: int) -> list:
    mask = 1 << (bits-1)
    rows = []
    for row in template:
        rows.append([])
        for pixel in row:
            if pixel is None:
                rows[-1].append(None)
            else:
                rows[-1].append(compressed & mask != 0)
                compressed = compressed << 1
    return rows


neighbors = [(-1, -1), (1, -1), (-2, 0), (0, 0), (2, 0), (1, 1), (-1, 1)]


def make_flip_mask_map(template: list) -> dict:
    mask_map = dict()
    for i in range(bits):
        compressed = 1 << i
        rows = uncompress(template, compressed)
        for y, row in enumerate(rows):
            for x, pixel in enumerate(row):
                if pixel == True:
                    bx, by = x, y
                    break
        for dx, dy in neighbors:
            if rows[by+dy][bx+dx] != None:
                rows[by+dy][bx+dx] = True
        mask = compress(rows)
        mask_map[compressed] = mask
    return mask_map


def make_template() -> list:
    global bits
    with open('image.dat') as f:
        data = f.read()[1+len(header):-1]

    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(data))

    image_surface = load("imageToSave.png")
    bits = 37

    start_x, start_y = 260, 153
    hex_w, hex_h = 60, 69
    dx = hex_w / 2
    dy = hex_h * 0.75

    template = list()
    template.append([None] * 20)
    for y in range(4):
        row = [None] * (6-y)
        for x in range(y + 4):
            bx = int(start_x - y * dx + x * hex_w)
            by = int(start_y + y * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (6-y)
        template.append(row)
    for y in range(3):
        row = [None] * (4+y)
        for x in range(6 - y):
            bx = int(start_x - (2 - y) * dx + x * hex_w)
            by = int(start_y + (4 + y) * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (4+y)
        template.append(row)
    template.append([None] * 20)

    return template


def print_template(template: list):
    for row in template:
        for pixel in row:
            if pixel == True:
                print('1', end='')
            elif pixel == False:
                print('0', end='')
            else:
                print(' ', end='')
        print()


def heuristic(compressed: int) -> int:
    # count bits set
    count = 0
    n = compressed

    while (n):
        n &= (n-1)
        count += 1

    return min(count, bits - count)

def draw_puzzle(screen, template, puzzle, radius, x_offset):
    rows = uncompress(template, puzzle)
    for y, row in enumerate(rows):
        for x, pixel in enumerate(row):
            if pixel == True:
                pygame.draw.circle(screen, (244, 199, 116), (x * radius + x_offset, y * 2 * radius), radius)
            elif pixel == False:
                pygame.draw.circle(screen, (107, 85, 128), (x * radius + x_offset, y * 2 * radius), radius)


def update_screen(screen, myfont, template: list, compressed: int) -> bool:
    radius = 20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                return False

    screen.fill((0, 0, 0))

    draw_puzzle(screen, template, compressed, radius, 0)

    pygame.display.flip()

    return True

def a_star(compressed: int, template: list):
    open_node = [(heuristic(compressed), 0, compressed, 0)]
    counter = 0
    closed_node = set()

    if graphics:
        pygame.init()
        pygame.font.init()

        size = 640, 480
        screen = pygame.display.set_mode(size)

        myfont = pygame.font.SysFont('verdana', 32)

    running = True

    while running and open_node:
        counter += 1

        _, step, compressed, moves = heapq.heappop(open_node)
        closed_node.add(compressed)

        if counter % 1000 == 0:
            if graphics:
                running = update_screen(screen, myfont, template, compressed)
            else:
                print(f"{compressed:b}".replace('0', '.').replace('1', '>'), end='\r')

        if heuristic(compressed) == 0:
            if graphics:
                update_screen(screen, myfont, template, moves)
            print(
                f"Found solution in {step} steps after examining {counter} nodes")
            print_template(uncompress(template, moves))
            break

        # add all neighbors to open list
        for mask_index in mask_map:
            # if this move was already made, skip it
            if mask_index & moves:
                continue
            mask = mask_map[mask_index]
            new_compressed = compressed ^ mask
            h = heuristic(new_compressed)
            # if this move would not flip any bits, skip it
            if h and (new_compressed & mask == 0 or new_compressed & mask == mask):
                continue
            # if this solution has already been found, skip it
            if new_compressed not in closed_node:
                heapq.heappush(open_node, (h + step + 1, step + 1,
                                           new_compressed, moves | mask_index))
                closed_node.add(new_compressed)
    
    while graphics and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break


if __name__ == "__main__":
    # read -g switch from command line
    if len(sys.argv) > 1 and sys.argv[1] == "-g":
        graphics = True

    template = make_template()
    print_template(template)
    compressed = compress(template)
    mask_map = make_flip_mask_map(template)

    a_star(compressed, template)
