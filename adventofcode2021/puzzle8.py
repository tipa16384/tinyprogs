# ticking away the moments that make up a dull day
# fritter and waste the hours in an off-hand way
# kicking around on a piece of ground in your home town
# waiting for someone or something to show you the way

number_segs = { 'abcefg': '0', 'cf': '1',  'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
                'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9' }

# read 'puzzle8.dat' and yield each line
def read_input():
    with open('puzzle8.dat') as f:
        for line in f:
            yield line.strip()

# parse a line into a list of ten words, followed by '|', and four more words
def parse_line(line):
    words = line.split(' ')
    return words[:10], words[10], words[11:15]

def figure_it_out(sample):
    decrypt_map = {}
    one = [x for x in sample if len(x) == 2][0]
    seven = [x for x in sample if len(x) == 3][0]
    four = [x for x in sample if len(x) == 4][0]
    top = [x for x in seven if x not in one][0]

    decrypt_map[top] = 'a'

    for word in sample:
        if len(word) == 5 and top in word and one[0] in word and one[1] in word:
            three = word
    
    for letter in four:
        if letter not in three:
            upper_left = letter
            decrypt_map[upper_left] = 'b'

    for word in sample:
        if len(word) == 5 and top in word and ((one[0] in word) ^ (one[1] in word)) and upper_left not in word:
            two = word 
            upper_right = one[0] if one[0] in word else one[1]
            lower_right = one[1] if one[0] in word else one[0]
            break
    
    for word in sample:
        if len(word) == 5 and word != two:
            five = word
    
    for letter in two:
        if letter not in five and letter != upper_right:
            lower_left = letter
            decrypt_map[lower_left] = 'e'

    for letter in four:
        if letter not in [upper_right, upper_left, lower_right]:
            middle = letter
            decrypt_map[middle] = 'd'
    
    for letter in three:
        if letter not in [top, upper_right, middle, lower_right]:
            bottom = letter
            decrypt_map[bottom] = 'g'

    decrypt_map[upper_right] = 'c'
    decrypt_map[lower_right] = 'f'

    return decrypt_map

def translate_word(word, decrypt_map):
    return ''.join([decrypt_map[letter] for letter in word])

def sort_letters_in_word(word):
    return ''.join(sorted(word))

def score_word(word):
    "return count of 1, 4, 7 and 8"
    return sum(1 for letter in word if letter in '1478')

score = 0
total = 0

for line in read_input():
    sample, pipe, output = parse_line(line)
    decrypt_map = figure_it_out(sample)
    display = ''
    for word in output:
        translated = translate_word(word, decrypt_map)
        digit = number_segs[sort_letters_in_word(translated)]
        display += digit
        if digit in '1478':
            score += 1
    total += int(display)

print (score)
print (total)
