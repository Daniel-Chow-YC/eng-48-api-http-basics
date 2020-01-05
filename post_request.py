import requests
import json

# To make a POST request we need:
    #1) URL
        # a) path + arguments
    #2)JSON

# URL
path = 'http://api.postcodes.io/postcodes/'
arguments = '' #this is what our documentation overlords asked of us - nothing
url = path + arguments

post_code = requests.get(url)
print(post_code)