import base64
import pygame
import heapq
from functools import lru_cache, reduce

header = 'data:image/png;base64,'
bits = 0

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

neighbors = [(-1,-1), (1, -1), (-2, 0), (0, 0), (2, 0), (1, 1), (-1, 1)]

def make_flip_mask_map(template: list) -> dict:
    mask_map = dict()
    for i in range(bits):
        compressed = 1 << i
        rows = uncompress(template, compressed)
        for y, row in enumerate(rows):
            for x, pixel in enumerate(row):
                if pixel == True:
                    bx, by = x, y
                    # print (bx, by)
                    break
        for dx, dy in neighbors:
            #print (bx, by, dx, dy)
            #print (rows[by+dy][bx+dx])
            if rows[by+dy][bx+dx] != None:
                rows[by+dy][bx+dx] = True
        mask = compress(rows)
        mask_map[compressed] = mask
    return mask_map

def make_template_very_hard() -> list:
    global bits
    with open('image.dat') as f:
        data = f.read()[1+len(header):-1]

    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(data))

    image_surface = pygame.image.load("imageToSave.png")
    bits = 61

    start_x, start_y = 243, 124
    hex_w, hex_h = 53, 62
    dx = hex_w / 2
    dy = hex_h * 0.75

    template = list()
    template.append([None] * 20)
    for y in range(5):
        row = [None] * (7-y)
        for x in range(y + 5):
            bx = int(start_x - y * dx + x * hex_w)
            by = int(start_y + y * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (7-y)
        template.append(row)
    for y in range(4):
        row = [None] * (4+y)
        for x in range(8 - y):
            bx = int(start_x - (3 - y) * dx + x * hex_w)
            by = int(start_y + (5 + y) * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (4+y)
        template.append(row)
    template.append([None] * 20)
    
    return template

def make_template_hard() -> list:
    global bits
    with open('image.dat') as f:
        data = f.read()[1+len(header):-1]

    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(data))

    image_surface = pygame.image.load("imageToSave.png")
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

def make_template_medium() -> list:
    global bits
    with open('image.dat') as f:
        data = f.read()[1+len(header):-1]

    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(data))

    image_surface = pygame.image.load("imageToSave.png")
    bits = 19

    start_x, start_y = 271, 174
    hex_w, hex_h = 81, 91
    dx = hex_w / 2
    dy = hex_h * 0.75

    template = list()
    template.append([None] * 20)
    for y in range(3):
        row = [None] * (5-y)
        for x in range(y + 3):
            bx = int(start_x - y * dx + x * hex_w)
            by = int(start_y + y * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (5-y)
        template.append(row)
    for y in range(2):
        row = [None] * (4+y)
        for x in range(4 - y):
            bx = int(start_x - (1 - y) * dx + x * hex_w)
            by = int(start_y + (3 + y) * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (4+y)
        template.append(row)
    template.append([None] * 20)
    
    return template

def make_template_easy() -> list:
    global bits

    with open('image.dat') as f:
        data = f.read()[1+len(header):-1]

    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(data))

    image_surface = pygame.image.load("imageToSave.png")

    start_x, start_y = 254, 230
    hex_w, hex_h = 96, 111
    dx = hex_w / 2
    dy = hex_h * 0.75
    bits = 10

    template = list()
    template.append([None] * 13)
    for y in range(2):
        row = [None] * (3-y)
        for x in range(y + 3):
            bx = int(start_x - y * dx + x * hex_w)
            by = int(start_y + y * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (3-y)
        template.append(row)
    for y in range(1):
        row = [None] * (3-y)
        for x in range(3 - y):
            bx = int(start_x - y * dx + x * hex_w)
            by = int(start_y + (2 + y) * dy)
            row.append(image_surface.get_at((bx, by))[0] > 128)
            row.append(None)
        row += [None] * (3-y)
        template.append(row)
    template.append([None] * 13)
    
    return template

def print_template(template: list):
    for row in template:
        for pixel in row:
            if pixel == True:
                print ('1', end='')
            elif pixel == False:
                print ('0', end='')
            else:
                print (' ', end='')
        print ()

# @lru_cache
def heuristic(compressed: int) -> int:
    # count bits set
    count = 0
    n = compressed

    while (n):
        n &= (n-1)
        count += 1

    return min(count, bits - count)

def heuristic_new(compressed: int) -> int:
    score = len(mask_map)

    for mask in mask_map.values():
        if (mask & compressed == mask) or (mask & compressed == 0):
            score -= 1

    return score

def zheuristic(compressed: int) -> int:
    return 0

def a_star():
    global compressed

    open_node = [(heuristic(compressed), 0, compressed, 0)]
    counter = 0
    closed_node = set()
    running = True

    while running and open_node:
        counter += 1

        val, step, compressed, moves = heapq.heappop(open_node)
        closed_node.add(compressed)

        if counter % 1000 == 0:
            print (f"{counter}, {val}, {step}, {len(open_node)}, {compressed:b}")
        
        # if counter % 100000 == 0:
        #     closed_node.clear()

        if heuristic(compressed) == 0:
            print (f"Found solution in {step} steps after examining {counter} nodes, end state {compressed:b}")
            print_template(uncompress(template, moves))
            break
        
        for mask_index in mask_map:
            if mask_index & moves: continue
            mask = mask_map[mask_index]
            new_compressed = compressed ^ mask
            h = heuristic(new_compressed)
            if h and (new_compressed & mask == 0 or new_compressed & mask == mask):
                continue
            if new_compressed not in closed_node:
                heapq.heappush(open_node, (h + step + 1, step + 1, new_compressed, moves | mask_index))
                closed_node.add(new_compressed)

template = make_template_hard()
print_template(template)
compressed = compress(template)
rows = uncompress(template, compressed)
recompressed = compress(rows)
assert compressed == recompressed
mask_map = make_flip_mask_map(template)

a_star()

# ..###..
# .####.
# ..###..

