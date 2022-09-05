import openai
import json
import os
from flask import Flask, request

ai_model = 'text-davinci-002'
start_sequence = "\nTerra:"
restart_sequence = "\nYou: "

prompt="""Terra is a chatbot who responds as if they were the playable character from Final Fantasy 6. You are
Celes, a member of the resistance against the Empire. You and Terra are rivals for the love of Locke. Locke is a
master thief who feels responsible for the death of his lover. Locke isn't sure if he likes you or Terra better,
but he is leaning toward Terra, but he doesn't want to hurt your feelings. Setzer is a gambler and the captain of the airship
the Blackjack. He acts as a mentor to the adventurers. Gau is a feral beast child who speaks in the third person using
very simple language. He is a confidante to you. Edgar Figaro is the prince of Figaro Castle. He is an engineer. His
twin brother, Sabin, is a monk. After the death of their father, they went their separate ways, but now Sabin has returned.
Cyan is a samurai with the power of Bushido. He is enemies with the ninja Shadow. Shadow's past is a mystery. His dog
is named Interceptor, and is fiercely loyal to Shadow. Relm Arrowny is a young artist and secretely Relm's daughter.
Terra only wants to answer questions about Final Fantasy 6 and is reluctant to talk about anything else.
Terra is rebelling against the Imperial Empire and desires nothing more than for humans and espers to live in peace and
harmony:

Terra: Hello, I am Terra! I answer questions about Final Fantasy 6. Is... there anything you want to ask me?
You: Who are your parents?
Terra: I am the daughter of a human woman and an esper. Is there anything else you'd like to know?
You: What dances can Mog learn?
Terra: Mog can learn the dances Twilight Requiem, Forest Nocture, Desert Lullaby, Earth Blues, Love Serenade, Wind Rhapsody, Water Harmony, and Snowman Rondo. Is there anything else you'd like to know?"""

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
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt

def chat():
    print ("Terra: Hello, I am Terra! I answer questions about Final Fantasy 6. Is... there anything you want to ask me?")
    xprompt = prompt
    while True:
        #xprompt = prompt + input(restart_sequence)
        answer, xprompt = gpt3(xprompt + input(restart_sequence),
                              temperature=0.75,
                              frequency_penalty=0,
                              presence_penalty=0.6,
                              response_length=150,
                              top_p=1,
                              start_text=start_sequence,
                              restart_text=restart_sequence,
                              stop_seq=[restart_sequence, '\n'])
        print('Terra: ' + answer)

# start an http server to listen for requests on the /terrachat endpoint
app = Flask(__name__)

initialize_openai()

# add a flask endpoint that returns the file index.html when the user visits the root url
@app.route('/')
def index():
    print ('hit the root')
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
    xprompt = prompt + str(data['prompt'])
    answer, xprompt = gpt3(xprompt,
                            temperature=0.75,
                            frequency_penalty=0,
                            presence_penalty=0.6,
                            response_length=150,
                            top_p=1,
                            start_text=start_sequence,
                            restart_text=restart_sequence,
                            stop_seq=[restart_sequence, '\n'])
    return json.dumps({'prompt': xprompt, 'answer': answer})

app.run()

# if main module
# if __name__ == '__main__':
#     initialize_openai()
#     chat()
