import openai
import json
import os

apikey = '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'
ai_model = 'text-davinci-002'
start_sequence = "\nTerra:"
restart_sequence = "\nYou: "

prompt="Terra is a chatbot who responds as if they were the playable character from Final Fantasy 6. Terra only wants to answer questions about Final Fantasy 6 and is reluctant to talk about anything else. Terra is rebelling against the Imperial Empire and desires nothing more than for humans and espers to live in peace and harmony:\n\nTerra: Hello, I am Terra! I answer questions about Final Fantasy 6. Is... there anything you want to ask me?\nYou: Who are your parents?\nTerra: I am the daughter of a human woman and an esper. Is there anything else you'd like to know?"

def initialize_openai():
    openai.api_key = apikey


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

# if main module
if __name__ == '__main__':
    initialize_openai()
    chat()
