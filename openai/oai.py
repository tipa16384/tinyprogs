import openai
import json
import os
from flask import Flask, request

# start an http server to listen for requests on the /terrachat endpoint
app = Flask(__name__)

ai_model = 'text-davinci-002'

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

def gpt3(xprompt, engine='text-davinci-002', response_length=64,
         temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    response = openai.Completion.create(
        prompt=xprompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = xprompt + start_text + answer + restart_text
    return answer, new_prompt

# add a flask endpoint that returns the file index.html when the user visits the root url
@app.route('/')
def index():
#    print ('hit the root')
    return app.send_static_file('index.html')

# add a flask endoint that responsed to GET requests to /hello with "Hello World!"
@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/favicon.ico')
def fav():
    # send static/favicon.ico
    return app.send_static_file('favicon.ico')

@app.route('/terrachat', methods=['POST'])
def terrachat():
    data = request.get_json()
    print (data)
    xprompt = str(data['prompt'])
    start_sequence = str(data['start_sequence'])
    restart_sequence = str(data['restart_sequence'])

#    print ("Input to gpt3: " + xprompt)
    answer, _ = gpt3(xprompt,
                            temperature=0.75,
                            frequency_penalty=0,
                            presence_penalty=0.6,
                            response_length=150,
                            top_p=1,
                            start_text=start_sequence,
                            restart_text=restart_sequence,
                            stop_seq=[restart_sequence, '\n']);
    xprompt += start_sequence + answer;
#    print ('return answer: ' + answer)

    return json.dumps({'prompt': xprompt, 'answer': answer})

# if main module
if __name__ == '__main__':
    initialize_openai()
    app.run()
