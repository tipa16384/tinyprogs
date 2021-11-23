#!/usr/bin/python

import os
import sys

dict_file = '/usr/share/dict/words'
wordle_file = 'wordle.txt'


def create_wordle_file():
    """
    wordle_file is a test file that contains the words from dict_file
    that are all lower case and exactly five letters long
    """
    if not os.path.exists(wordle_file):
        print("Creating %", wordle_file)
        with open(dict_file, 'r') as f:
            with open(wordle_file, 'w') as g:
                for line in f:
                    word = line.strip()
                    if len(word) == 5 and word.islower():
                        g.write(word + '\n')


def get_wordle_list():
    "return a list of words from wordle_file"
    create_wordle_file()
    with open(wordle_file, 'r') as f:
        return [line.strip() for line in f]


def get_pairs(guess):
    "yield letter/position tuples from the guess"
    while guess:
        pair = (guess[0], guess[1])
        guess = guess[2:]
        yield pair


def contains_gray(word, gray):
    "return True if the word contains any letters in gray"
    for letter in gray:
        if letter in word:
            return True
    return False


def contains_green(word, green):
    "return True if the word does not contain a letter in the correct position."
    for (letter, position) in get_pairs(green):
        if word[int(position)] != letter:
            return True
    return False


def contains_yellow(word, yellow):
    "return True if the word contains the letter in the wrong position or the letter is not in the word."
    for (letter, position) in get_pairs(yellow):
        if word[int(position)] == letter or letter not in word:
            return True
    return False


def prune_words(word_list, f):
    "prune words from word_list that satisfy the predicate"
    remove_words = set()
    for word in word_list:
        if f(word):
            remove_words.add(word)
    for word in remove_words:
        word_list.remove(word)


def get_words_with_no_duplicates(word_list):
    "return the words from word_list that have no duplicate letters"
    unique_words = []
    for word in word_list:
        letter_set = set([y for y in word])
        if len(letter_set) == 5:
            unique_words.append(word)
    return unique_words


def choose_word(word_list):
    "choose the word from word_list that has the highest weight of popular letters"
    # create a dictionary of letter counts
    letter_counts = {}
    for word in word_list:
        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    # weight words by the product of their letter counts
    weights = {}
    for word in word_list:
        weight = 1
        for letter in word:
            weight *= letter_counts[letter]
        weights[word] = weight
    # sort the words by weight high to low
    sorted_words = sorted(
        weights.keys(), key=lambda x: weights[x], reverse=True)
    # return the first word in the sorted list
    return sorted_words[0]


def run_test():
    "unit tests"
    word_list = get_wordle_list()
    assert game_loop(word_list, ',r1e4,ais', True) == 'arise'
    assert game_loop(word_list, ',e3r4,out', True) == 'outer'
    assert game_loop(word_list, 'e1,r0,dly', True) == 'redly'


def game_loop(word_list, guess=None, quiet=False):
    uniques = get_words_with_no_duplicates(word_list)
    unique_length = len(uniques)
    if not uniques:
        uniques = word_list
    if not uniques:
        if not quiet:
            print("No words left")
        sys.exit(1)
    # choose a word from uniques
    word = choose_word(uniques)
    # prompt the user with the word
    if not quiet:
        print("%d uniques, %d total words" % (unique_length, len(word_list)))
        print("Try this word (respond with green, yellow, gray letters):", word)

    # get the user's guess
    if not guess:
        guess = input("Wordle says: ").strip()

    if not guess:
        sys.exit(0)
    try:
        (green, yellow, gray) = guess.split(',')
        prune_words(word_list, lambda x: contains_gray(x, gray)
                    or contains_green(x, green) or contains_yellow(x, yellow))
    except:
        if not quiet:
            print("Invalid guess")
        else:
            assert False

    return word


def play_game():
    run_test()
    word_list = get_wordle_list()
    while True:
        game_loop(word_list)


if __name__ == '__main__':
    play_game()
