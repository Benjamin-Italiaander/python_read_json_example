# Python example to read all data from a json file
# This example i use as a basic for all my python json vars
# In this example i use it for a multilanguage website.

import json

# In this case i specify to read all content from the NL language
language = 'NL'
print(language)

# Defining JSON file to var f
f = open('content.json')
 
# load var f to json.load object as a dictionary in data
data = json.load(f)

# Reading HEADER from language NL  
for i in data['HEADER']:
    for key, value in i.items():
        if key == language:
            print(value)

# Reading BODY from language NL
for i in data['BODY']:
    for key, value in i.items():
        if key == language:
            print(value)

# Closing file
f.close()
