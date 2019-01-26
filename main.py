import requests

# Getting info from the pokemon API and save the data as request objects
r = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu', )
# Convert to json
json_response = r.json()
# Create a file called Json.txt and save it in the current directory, use the "output_file" as a pointer to Json.txt
with open("json.txt", mode='w') as output_file:
# This is a loop, firstly it picks up the first key, then the second key and so on
    for k in json_response.keys():
# Dumps the keys and values to the Json.txt to the pointer
       print(k, json_response.get(k), file=output_file)