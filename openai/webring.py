import json
import random

def lambda_handler(event, context):
   # List of URLs to choose from
    url_list = [
        "dragonchasers.com",
        "bhagpuss.blogspot.com",
        "scopique.com",
        "tagn.wordpress.com",
        "thefriendlynecromancer.blogspot.com",
        "massivelyop.com",
        "nomadicgamer.ca",
        "aggronaut.com",
        "aywren.com",
        "www.heartlessgamer.com",
        "biobreak.wordpress.com",
        "endgameviable.com",
        "chasingdings.com"
    ]

    # Check if 'exclude' parameter is present in the query string
    parms = event.get('queryStringParameters', {}) if event else None
    exclude = parms.get('exclude') if parms else None
    # if exclude is not in the list, set it to None
    if exclude not in url_list:
        exclude = None
    # if a parameter named 'next' is present, set the variable next to True, else False
    next_site = True if parms and parms.get('next') else False
    prev_site = True if parms and parms.get('prev') else False
    
    # if next_site is True and exclude exists, then redirect_url is the next site in the list, wrapping around if necessary
    if next_site and exclude:
        redirect_url = url_list[(url_list.index(exclude) + 1) % len(url_list)]
    elif prev_site and exclude:
        redirect_url = url_list[(url_list.index(exclude) - 1) % len(url_list)]
    else:
        redirect_url = random.choice(list(filter(lambda x: x != exclude, url_list)))

    # Return a 302 redirect response
    return {
        'statusCode': 302,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # Allow all origins, you can restrict as needed
            'Location': 'https://' + redirect_url + '/'
        },
        'body': ''
    }
