import openai
import json
import os
from flask import Flask, request
from squaredle import find_words
import re

# start an http server to listen for requests on the /terrachat endpoint
application = Flask(__name__)

ai_model = 'gpt-4'
word_set = None

def initialize_openai():
    # read the api key from the environment variable OPENAI_API_KEY
    # or from the file openai_api_key.txt
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        try:
            with open('openai_api_key.txt') as f:
                api_key = f.read().strip()
        except FileNotFoundError:
            print('Please set the OPENAI_API_KEY environment variable or create a file openai_api_key.txt with your OpenAI API key in it.')
            exit(1)
    openai.api_key = api_key

def get_models():
    models = openai.Model.list()
    models_dict = models.to_dict()
    model_list = models_dict['data']

    return [model.id for model in model_list]

def gptturbo(messages, response_length=1024,
         temperature=0.7, top_p=1, frequency_penalty=0.7, presence_penalty=0.3):
    response = openai.ChatCompletion.create(model = ai_model, messages = messages,
                                            max_tokens=response_length,
                                            temperature=temperature,
                                            top_p=top_p,
                                            frequency_penalty=frequency_penalty,
                                            presence_penalty=presence_penalty)
    return response

def find_regex(start, end, length):
    global word_set
    
    start = '' if start == '?' else start.replace('?', '').lower()
    end = '' if end == '?' else end.replace('?', '').lower()
    length = int(length) if length.isnumeric() else 0

    if length:
        length = length - len(start) - len(end)
    
    regex = f'^{start}.*{end}$' if not length else f'^{start}.{{{length}}}{end}$'

    print (regex)

    # find all words that match the regex
    answers = [word for word in word_set if re.match(regex, word)]

    return 'Being sure to include all these words in your response, please tell the user that they might like these words: ' + ', '.join(answers) if answers else 'Please tell the user that no words were found.'


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

@application.route('/terrachat', methods=['POST'])
def terrachat():
    data = request.get_json()
    # print (data)
    # convert data['messages'] from JSON to an array of dict

    messages =data['messages']
    response = gptturbo(messages)
    terra_says = response['choices'][0]['message']['content'];

    if 'REGEX' in terra_says:
        print ("Terra says: " + terra_says)
        # parse the string REGEX a,b,c from terra_says
        m = re.search('REGEX (.*),(.*),(\?|\d+)', terra_says)
        if m:
            print (terra_says)
            print (m.group(1), m.group(2), m.group(3))
            # remove the last entry from messages
            messages.pop()
            terra_says = find_regex(m.group(1), m.group(2), m.group(3))
            messages.append({ 'role': 'system', 'content': terra_says })
            response = gptturbo(messages)
            print (response)
            print (dir(response))
            terra_says = response['choices'][0]['message']['content'];
            messages.pop()
    else:
        messages.append({ 'role': 'assistant', 'content': terra_says })

    print (messages)

    return json.dumps({'answer': terra_says, 'conversation': messages})

# if main module
if __name__ == '__main__':
    initialize_openai()
    application.run()
