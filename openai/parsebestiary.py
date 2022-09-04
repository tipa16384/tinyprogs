
import re
import json
import csv

record_divider = '********************************************************************************'

simple_keys = ['Level: ', 'HP: ', 'MP: ', 'Attack: ', 'Defense: ', 'Magic: ',
                'Magic Defense: ', 'Magic Evasion: ', 'Speed: ', 'EXP: ', 'Gil: ', 'Drops: ', 'Steal: ', 'Elemental Immunity: ',
                'Absorbs: ', 'Type: ', 'Status Immunity: ', 'Status Vulnerability: ', 'Inherent Status: ', 'Other Immunity: ',
                'Special Attack: ', 'Rage: ', 'Sketch: ', 'Control: ', 'Metamorphose: ', 'Imp Criticals: ', 'Run Difficulty: ']



def bst_parse(record):
    beast = {}
    scanning_for_location = False
    scanning_for_weakness = False
    # scan for a line that starts with a number, a period, and a space
    for l in record.splitlines():
        l = l.strip()
        if not l:
            scanning_for_location = False
            scanning_for_weakness = False
            continue
        if scanning_for_location:
            beast['location'] += ' ' + l
            continue
        if scanning_for_weakness:
            beast['weakness'] += ', ' + l
            continue
        m = re.match(r'^\d+\.\s', l)
        if m:
            match_len = len(m.group(0))
            name = l[match_len:]
            if 'No Name' == name:
                return None
            # remove any string matching [...]
            name = re.sub(r'\s\[.*\]', '', name)
            beast['name'] = name
            continue
        # if starts with SNES Name:
        m = re.match(r'^SNES Name:\s', l)
        if m:
            match_len = len(m.group(0))
            snes_name = l[match_len:]
            if snes_name and snes_name != beast['name']:
                beast['snes_name'] = snes_name
            continue
        # if starts with Location: 
        m = re.match(r'^Location:\s', l)
        if m:
            match_len = len(m.group(0))
            location = l[match_len:]
            if location and location != 'Unknown':
                beast['location'] = location
                scanning_for_location = True
            continue
        # if starts with Vulnerable to: 
        m = re.match(r'^Vulnerable to:\s', l)
        if m:
            match_len = len(m.group(0))
            weakness = l[match_len:]
            if weakness and weakness != 'Nothing':
                beast['weakness'] = weakness
                scanning_for_weakness = True
            continue
        # if starts with any key in simple_keys
        for k in simple_keys:
            if l.startswith(k):
                val = l[len(k):]
                if val and val != 'None' and val != 'N/A':
                    beast[k.strip(': ')] = val
                break

    return beast

def process(beast):
    # prompts is a list of tuples
    prompts = []

    name = beast['name']
    if 'snes_name' in beast:
        prompts.append(('What is the ' + name + ' known as on the SNES?', beast['snes_name'] ))
    if 'weakness' in beast:
        prompts.append(('What is the weakness of the ' + name + '?', beast['weakness'] ))
    if 'location' in beast:
        prompts.append(('Where is the ' + name + ' located?', beast['location'] ))
    if 'Drops' in beast:
        prompts.append(('What does the ' + name + ' drop?', beast['Drops'] ))
    if 'Steal' in beast:
        prompts.append(('What can be stolen from the ' + name + '?', beast['Steal'] ))
    if 'Type' in beast:
        prompts.append(('What type of monster is the ' + name + '?', beast['Type'] ))
    if 'Special Attack' in beast:
        prompts.append(('What is the special attack of the ' + name + '?', beast['Special Attack'] ))
    if 'Status Immunity' in beast:
        prompts.append(('What status effects does the ' + name + ' resist?', beast['Status Immunity'] ))
    if 'Absorbs' in beast:
        prompts.append(('What status effects does the ' + name + ' absorb?', beast['Absorbs'] ))
    if 'HP' in beast:
        prompts.append(('How much HP does the ' + name + ' have?', beast['HP'] ))
    if 'Rage' in beast:
        prompts.append(('What rage can be learned from the ' + name + '?', beast['Rage'] ))
    if 'Sketch' in beast:
        prompts.append(('What sketch can be drawn from the ' + name + '?', beast['Sketch'] ))
    if 'Control' in beast:
        prompts.append(('What abilities can be used while controlling the ' + name + '?', beast['Control'] ))
    if 'Elemental Immunity' in beast:
        prompts.append(('What elements does the ' + name + ' resist?', beast['Elemental Immunity'] ))

    return prompts

def process2(beast):
    # prompts is a list of tuples
    prompts = []

    name = beast['name']
    prompts.append('{} is an enemy in Final Fantasy VI.'.format(name))
    if 'snes_name' in beast:
        prompts.append('The SNES version of {} is known as {}.'.format(name, beast['snes_name']))
    if 'weakness' in beast:
        prompts.append('The weakness of {} is {}.'.format(name, beast['weakness']))
    if 'location' in beast:
        prompts.append('{} is located in {}.'.format(name, beast['location']))
    if 'Drops' in beast:
        prompts.append('{} drops {}.'.format(name, beast['Drops']))
    if 'Steal' in beast:
        prompts.append('{} can be stolen from {}.'.format(beast['Steal'], name))
    if 'Type' in beast:
        prompts.append('{} is a {} type monster.'.format(name, beast['Type']))
    if 'Special Attack' in beast:
        prompts.append('The special attack of {} is {}.'.format(name, beast['Special Attack']))
    if 'Status Immunity' in beast:
        prompts.append('{} resists the following status effects: {}.'.format(name, beast['Status Immunity']))
    if 'Absorbs' in beast:
        prompts.append('{} absorbs the following status effects: {}.'.format(name, beast['Absorbs']))
    if 'HP' in beast:
        prompts.append('{} has {} HP.'.format(name, beast['HP']))
    if 'Rage' in beast:
        prompts.append('Gau can learn the rage {} from {}.'.format(beast['Rage'], name))
    if 'Sketch' in beast:
        prompts.append('Relm can draw the sketch {} from {}.'.format(beast['Sketch'], name))
    if 'Control' in beast:
        prompts.append('The following abilities can be used while controlling {}: {}.'.format(name, beast['Control']))
    if 'Elemental Immunity' in beast:
        prompts.append('{} resists the following elements: {}.'.format(name, beast['Elemental Immunity']))

    return prompts


records = []

# open the file
with open('bestiary.faq', 'r') as f:
    # read the file into a string
    faq = f.read()
    read_records = faq.split(record_divider)
    # discard the first and last records
    read_records.pop(0)
    read_records.pop()
    # create a list of dictionaries
    for record in read_records:
        beast = bst_parse(record)
        if beast:
            records.append(beast)

# open a csv file for writing called kt2.csv
with open('kt2.csv', 'w', newline='') as f:
    # create the csv writer object
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # write a row to the csv file
    writer.writerow(['prompt', 'completion'])
    # iterate over the records
    for beast in records:
        # get the prompts
        prompts = process2(beast)
        # write each prompt to the csv file
        writer.writerow([beast['name']+'###',' ' + ' '.join(prompts) + '###'])

# print ("prompt,completion")
# for beast in records:
#     prompts = process2(beast)
#     print ('"","{}"'.format(' '.join(prompts)))
    #for prompt in prompts:
        #print ('{"prompt": "' + prompt[0] + '", "completion":"' + prompt[1] + '"}')
        #print ('"' + prompt[0] + '","' + prompt[1] + '"')
        #print ('"", "' + prompt + '"')



