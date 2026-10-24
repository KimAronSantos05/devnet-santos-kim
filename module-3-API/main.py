import requests
import random

def get_response():
    response = requests.get(
       'https://pokeapi.co/api/v1/pokemon?limit=5',
    )
    return response.json()

print ("==========WHO'S THAT POKEMON?==========")

print (" ")

pokemons_attribute = [
    "bulbasaur",
    "ivysaur",
    "venusaur",
    "charmander",
    "charmeleon",
]

print (random.choice(pokemons_attribute))
ask = input ("Type 'yes' to  process and 'no' to exit: ")

if ask == "yes":
    get_response()
elif ask == "no":
    print ("bye")