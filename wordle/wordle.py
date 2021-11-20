#!/usr/bin/python

import os
import random
import sys

dict_file = '/usr/share/dict/words'
wordle_file = 'wordle.txt'

# wordle_file is a test file that contains the words from dict_file
# that are all lower case and exactly five letters long
def create_wordle_file():
    if not os.path.exists(wordle_file):
        print ("Creating %", wordle_file)
        with open(dict_file, 'r') as f:
            with open(wordle_file, 'w') as g:
                for line in f:
                    word = line.strip()
                    if len(word) == 5 and word.islower():
                        g.write(word + '\n')

# return a list of words from wordle_file
def get_wordle_list():
    create_wordle_file()
    print ("Reading word list")
    with open(wordle_file, 'r') as f:
        return [line.strip() for line in f]

def get_pairs(guess):
    while guess:
        pair = (guess[0], guess[1])
        guess = guess[2:]
        yield pair

def remove_gray_letters(word_list, gray):
    remove_words = set()
    for word in word_list:
        for letter in gray:
            if letter in word:
                remove_words.add(word)
    for word in remove_words:
        word_list.remove(word)

def remove_yellow_letters(word_list, yellow):
    remove_words = set()
    for word in word_list:
        for (letter, position) in get_pairs(yellow):
            if word[int(position)] == letter or letter not in word:
                remove_words.add(word)
    for word in remove_words:
        word_list.remove(word)

def remove_green_letters(word_list, green):
    remove_words = set()
    for word in word_list:
        for (letter, position) in get_pairs(green):
            if word[int(position)] != letter:
                remove_words.add(word)
    for word in remove_words:
        word_list.remove(word)

# return the words from word_list that have no duplicate letters
def get_words_with_no_duplicates(word_list):
    unique_words = []
    for word in word_list:
        letter_set = set([y for y in word])
        if len(letter_set) == 5:
            unique_words.append(word)
    return unique_words

def play_game():
    word_list = get_wordle_list()
    while True:
        uniques = get_words_with_no_duplicates(word_list)
        unique_length = len(uniques)
        if not uniques:
            uniques = word_list
        if not uniques:
            print ("No words left")
            sys.exit(1)
        # choose a random word from uniques
        word = uniques[random.randint(0, len(uniques) - 1)]
        # prompt the user with the word
        print ("%d uniques, %d total words" % (unique_length, len(word_list)))
        print ("Try this word (respond with green, yellow, gray letters):", word)
        # get the user's guess
        guess = input("Wordle says: ")
        if not guess.strip():
            sys.exit(0)
        try:
            (green,yellow,gray) = guess.split(',')
            remove_gray_letters(word_list, gray)
            remove_yellow_letters(word_list, yellow)
            remove_green_letters(word_list, green)
        except:
            print ("Invalid guess")
            continue


if __name__ == '__main__':
    play_game()
