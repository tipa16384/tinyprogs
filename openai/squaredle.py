import re

class Letter:
    all_letters = []

    def __init__(self, letter, row, col):
        self.letter = letter
        self.row = row
        self.col = col
        self.adjacent = []

        for l in Letter.all_letters:
            if l.is_adjacent(self):
                l.add_adjacent(self)
                self.add_adjacent(l)
        
        Letter.all_letters.append(self)
    
    # return true if this letter is adjacent to other
    def is_adjacent(self, other):
        return abs(self.row - other.row) <= 1 and abs(self.col - other.col) <= 1

    # return true if this letter is at row, col
    def is_at(self, row, col):
        return self.row == row and self.col == col
    
    # get the adjacent letters
    def get_adjacent(self):
        return self.adjacent
    
    # add an adjacent letter
    def add_adjacent(self, letter):
        self.adjacent.append(letter)
    
    # return the letter
    def get_letter(self):
        return self.letter
    
    def __str__(self):
        return self.letter + ' -> ' + ''.join([l.get_letter() for l in self.adjacent])

def is_word_in_puzzle(word, letter, seen = []):
    if not word:
        return True
    if letter in seen:
        return False
    if word[0] != letter.get_letter():
        return False
    for l in letter.get_adjacent():
        if is_word_in_puzzle(word[1:], l, seen + [letter]):
            return True
    return False

def find_words():
    # read allgoodwords.txt into the list good_words
    with open('allgoodwords.txt', 'r') as f:
        good_words = [line.strip() for line in f]

    # read square.txt into the list puzzle
    with open('square.txt', 'r') as f:
        puzzle = [line for line in f]

    for row, line in enumerate(puzzle):
        for col, letter in enumerate(line):
            # create a Letter object for each letter in the puzzle
            letter = Letter(letter, row, col)

    # get the list of all letters
    letters = Letter.all_letters

    # make a map where the key is a letter and the value are all the letters that match
    letter_map = {}
    for letter in letters:
        if letter.get_letter() not in letter_map:
            letter_map[letter.get_letter()] = []
        letter_map[letter.get_letter()].append(letter)

    word_set = set()

    # for every word in good_words
    for word in good_words:
        # get the first letter
        first_letter = word[0]
        if first_letter not in letter_map:
            continue
        # get the list of letters that match the first letter
        first_letter_list = letter_map[first_letter]
        # for every letter in the list
        for letter in first_letter_list:
            if is_word_in_puzzle(word, letter):
                word_set.add(word)
    
    return word_set

if __name__ == '__main__':
    word_set = find_words()

    print ("I have found", len(word_set), "words in the puzzle.")

    # in a loop, ask the user for a regular expression. Return the matching words. If the input is empty, exit the loop.
    while True:
        regex = input('Enter a regular expression: ')
        if not regex:
            break
        if not regex[0].isalpha():
            print ("Invalid input.")
            continue
        answers = [word for word in word_set if re.match('^'+regex+'$', word)]
        if not answers:
            print ("No matches.")
        else:
            print ("Matches: " + ', '.join(answers))
