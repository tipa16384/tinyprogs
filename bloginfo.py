# Gets information from Chasing Dings!

import requests

# Site URI (I wrote this)
SITE_URI = "http://chasingdings.com"

# index route (I wrote this)
INDEX_ROUTE = "/wp-json/"

# Headers (I wrote this)
custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# Make an HTTP GET request to the index route
def get_index_route():
    response = requests.get(SITE_URI + INDEX_ROUTE, headers = custom_headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# print some site info
def print_site_info():
    site_info = get_index_route()
    if site_info is not None:
        print ('Blog name:', site_info['name']) # I wrote this
        print ('Blog description:', site_info['description'])
        print ('Blog URL:', site_info['url'])
    else:
        print ('Error getting site info')

if __name__ == '__main__':
    print_site_info()
