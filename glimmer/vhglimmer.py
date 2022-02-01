import base64
from pygame.image import load
from functools import reduce
import sys
import csv

header = 'data:image/png;base64,'
bits = 0
graphics = False

def make_hard_solutions() -> dict:
    hard_solutions = dict()

    hard_solutions['D1'] = [1 << 60, 1 << 55, 1 << 49, 1 << 42, 1 << 34]
    hard_solutions['D2'] = [1 << 59, 1 << 54, 1 << 48, 1 << 41, 1 << 33, 1 << 25]
    hard_solutions['D3'] = [1 << 58, 1 << 53, 1 << 47, 1 << 40, 1 << 32, 1 << 24, 1 << 17]
    hard_solutions['D4'] = [1 << 57, 1 << 52, 1 << 46, 1 << 39, 1 << 31, 1 << 23, 1 << 16, 1 << 10]
    hard_solutions['D5'] = [1 << 56, 1 << 51, 1 << 45, 1 << 38, 1 << 30, 1 << 22, 1 << 15, 1 << 9, 1 << 4]

    hard_solutions['R1'] = [1 << 60, 1 << 59, 1 << 58, 1 << 57, 1 << 56]
    hard_solutions['R2'] = [1 << 55, 1 << 54, 1 << 53, 1 << 52, 1 << 51, 1 << 50]
    hard_solutions['R3'] = [1 << 49, 1 << 48, 1 << 47, 1 << 46, 1 << 45, 1 << 44, 1 << 43]
    hard_solutions['R4'] = [1 << 42, 1 << 41, 1 << 40, 1 << 39, 1 << 38, 1 << 37, 1 << 36, 1 << 35]
    hard_solutions['R5'] = [1 << 34, 1 << 33, 1 << 32, 1 << 31, 1 << 30, 1 << 29, 1 << 28, 1 << 27, 1 << 26]

    return hard_solutions

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


neighbors = [(1, 1), (-1, -1), (1, -1), (-2, 0), (0, 0), (2, 0),(-1, 1)]

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

def make_solve_mask_map(template: list) -> dict:
    solve_map = dict()

    for i in range(bits):
        try:
            compressed = 1 << i
            rows = uncompress(template, compressed)
            for y, row in enumerate(rows):
                for x, pixel in enumerate(row):
                    if pixel == True:
                        other_rows = uncompress(template, 0)
                        fx, fy = neighbors[0]
                        pixel_2 = other_rows[y+fy][x+fx]
                        if pixel_2 != None:
                            other_rows[y+fy][x+fx] = True
                            solve_map[compressed] = compress(other_rows)
                            raise StopIteration
        except:
            pass

    return solve_map

def make_template() -> list:
    global bits
    with open('vhimage.dat') as f:
        data = f.read()[1+len(header):-1]

    with open("vhimageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(data))

    image_surface = load("vhimageToSave.png")
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

def print_compressed(template: list, compressed: int):
    rows = uncompress(template, compressed)
    print_template(rows)

def process_template(template: list, invert = False) -> int:
    mask_map = make_flip_mask_map(template)
    solve_map = make_solve_mask_map(template)
    compressed = compress(template)

    if invert: compressed ^= ((1 << bits) - 1)

    # record all the moves
    click_record = 0

    solution_mask = reduce(lambda x, y: x | y, solve_map.keys())

    while compressed & solution_mask:
        for i in range(bits):
            bit_test_mask = 1 << (bits-i-1)
            if compressed & bit_test_mask & solution_mask:
                down_right = solve_map[bit_test_mask]
                click_record ^= down_right
                compressed = compressed ^ mask_map[down_right]
                break
    
    solution_key = (compressed & 0x1F) << 4
    if compressed & 0x20:
        solution_key |= 0x8
    if compressed & 0x800:
        solution_key |= 0x4
    if compressed & 0x40000:
        solution_key |= 0x2
    if compressed & 0x4000000:
        solution_key |= 0x1
    
    display_key = f"{(compressed & 0x1F):05b} {(solution_key & 0xF):04b}"

    solutions = read_csv(display_key)

    hard_solutions = make_hard_solutions()

    for move in solutions:
        if move:
            for move_click in hard_solutions[move]:
                click_record ^= move_click
                compressed ^= mask_map[move_click]
    
    while compressed & solution_mask:
        for i in range(bits):
            bit_test_mask = 1 << (bits-i-1)
            if compressed & bit_test_mask & solution_mask:
                down_right = solve_map[bit_test_mask]
                click_record ^= down_right
                compressed = compressed ^ mask_map[down_right]
                break

    return click_record

def read_csv(key: str) -> list:
    fn = 'vhanswers.csv'
    with open(fn) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == key:
                return row[3:]

def count_bits(x: int) -> int:
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count

if __name__ == "__main__":
    # read -g switch from command line
    if len(sys.argv) > 1 and sys.argv[1] == "-g":
        graphics = True

    template = make_template()
    print_template(template)

    click_rec1 = process_template(template)
    click_rec2 = process_template(template, True)

    count_1 = count_bits(click_rec1)
    count_2 = count_bits(click_rec2)

    click_record = click_rec1 if count_1 <= count_2 else click_rec2
    print_compressed(template, click_record)



