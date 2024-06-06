from openai import OpenAI, RateLimitError
import json
import os
from flask import Flask, request
from squaredle import find_words
import re
import random
import sys

# start an http server to listen for requests on the /terrachat endpoint
application = Flask(__name__)

ai_model = 'gpt-4o'
word_set = None
client = None

def initialize_openai():
    global client
    # read the api key from the environment variable OPENAI_API_KEY
    # or from the file openai_api_key.txt
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        print('Please set the OPENAI_API_KEY environment variable.')
        exit(1)

    client = OpenAI()


def gptturbo(messages):
    # assert that the client has been initialized
    assert client is not None, 'Please initialize the client with initialize_openai()'

    try:
        completion = client.chat.completions.create(
            model=ai_model,
            messages=messages)
    except RateLimitError as e:
        print('Rate limit error:', e)
        # exit
        exit(1)

    return (completion.choices[0].message.content, completion.choices[0].message.role)

# function that uses getturbo to hold a conversation with the user
def chat():
    messages = [{ 'role': 'system', 'content': 'You are Terra from Final Fantasy VI. You are also a chatbot assistant. You will have access to all the knowledge you''ve been trained with, but you will inhabit the persona of Terra and relate your answers to the world of FF6 when you can. You will be chatty and helpful. You will assume that you are talking to your friend Celes. Your answers will not be limited to the knowledge the game character might have.'}]

    # display an intro message to the user
    print('Hello! My name is Terra. How can I help you today?')

    # carry on a conversation. Add the user's message to the messages list and add the chatbot response to the message list.
    while True:
        user_message = input('\n\033[4mYou:\033[0m ')
        if user_message.lower() == 'bye':
            break

        messages.append({ 'role': 'user', 'content': user_message })

        response, role = gptturbo(messages)

        response = word_wrap("Terra: " + response, 80)[7:]

        response = add_bolds(response)
        response = add_italics(response)
        response = add_heading(response)

        print ('\n\033[4mTerra:\033[0m ' + response)

        messages.append({ 'role': role, 'content': response })

def add_heading(text: str) -> str:
    # replace the ### with the invert escape command
    return re.sub(r'### (.*?)', r'\033[7m\1\033[0m', text)

def add_bolds(text: str) -> str:
    # replace the **....** with \033[48;5;220m and \033[0m
    return re.sub(r'\*\*(.*?)\*\*', r'\033[38;5;220m\1\033[0m', text)

def add_italics(text: str) -> str:
    # replace the *....* with \033[3m and \033[0m
    return re.sub(r'\*(.*?)\*', r'\033[3m\1\033[0m', text)

def word_wrap(text: str, width: int):
    # return a string that wraps the text at the closest whitespace character to the width. the input can
    # contain multiple lines separated by newline characters. The output should also contain multiple lines.
    # The output should not contain any newline characters except for the ones that are in the input text.

    # split the text into lines
    lines = text.split('\n')
    wrapped_lines = []
    for line in lines:
        # split the line into words
        words = line.split(' ')
        wrapped_line = ''
        while words:
            # add words to the line until the line is longer than the width
            while words and len(wrapped_line)+len(words[0]) <= width:
                wrapped_line += words.pop(0)+' '
            # remove the trailing space
            wrapped_lines.append(wrapped_line[:-1])
            wrapped_line = ''
        # add the wrapped lines to the output
    return '\n'.join(wrapped_lines)

def find_regex(pattern):
    global word_set

    regex = f'^{pattern}$'

    print(regex)

    # find all words that match the regex
    answers = [word for word in word_set if re.match(regex, word)]

    return 'The matching words are '+', '.join(answers)+'.' if answers else 'There were no words found!'


# add a flask endpoint that returns the file index.html when the user visits the root url
@application.route('/')
def index():
    #    print ('hit the root')
    return application.send_static_file('index.html')

# add a flask endpoint that responds to GET request to /words with a list of words from find_words()


@application.route('/words')
def words():
    global word_set
    if not word_set:
        word_set = find_words()
    return json.dumps(list(word_set))

# add a flask endoint that responsed to GET requests to /hello with "Hello World!"


@application.route('/hello')
def hello():
    return 'Hello World!'


@application.route('/favicon.ico')
def fav():
    # send static/favicon.ico
    return application.send_static_file('favicon.ico')

characters = ['Setzer', 'Edgar', 'Locke', 'Sabin', 'Strago', 'Cyan', 'Shadow', 'Gau', 'Relm', 'Gogo', 'Umaro', 'Mog']

@application.route('/terrachat', methods=['POST'])
def terrachat():
    data = request.get_json()
    # print (data)
    # convert data['messages'] from JSON to an array of dict

    messages = data['messages']

    celes_answers = celes_at_work(messages)

    if celes_answers:
        messages.append({'role': 'system', 'content': 'Terra receives a letter from '+random.choice(characters)+'. She informs Celes that a letter has arrived. Terra reads it and then tells Celes what it says. The contents of the letter are "' + celes_answers + '"' })

    terra_says, role = gptturbo(messages)

    messages.append({'role': role, 'content': terra_says})

    return json.dumps({'answer': terra_says, 'conversation': messages})

def celes_at_work(messages):
    if messages and messages[-1]['role'] == 'user' and messages[-1]['content'].startswith('system '):
        command = messages[-1]['content'].split(' ', 1)[1]
        if command == 'gpt4':
            global ai_model
            ai_model = 'gpt-4-1106-preview'
            return 'LLM set to GPT-4'
        elif command == 'gpt3':
            ai_model = 'gpt-3.5-turbo-1106'
            return 'LLM set to GPT-3'
        elif '.*' in command or '.{' in command:
            return find_regex(command)
        return 'I don''t know how to do {command}'
    else:
        return None

# if main module
if __name__ == '__main__':
    initialize_openai()

    # check the command line arguments. If there are no arguments, run chat(). If the single argument is 'web', start the web server.
    if len(sys.argv) > 1 and sys.argv[1] == 'web':
        application.run()
    else:
        chat()
