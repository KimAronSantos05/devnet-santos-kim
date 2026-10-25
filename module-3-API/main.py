import requests
import random

pokemon_list = ["pikachu", "charizard", "jigglypuff", "snorlax", "bulbasaur"]

def get_pokemon_data(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()

        name = data["name"]
        height = data["height"]
        weight = data["weight"]

        return name, height, weight

    else:
        print("Pokemon data not found.")
        return None

def play_game():
    print("==============================")
    print("   POKEMON GUESSING GAME")
    print("==============================")

    pokemon_name = random.choice(pokemon_list)

    result = get_pokemon_data(pokemon_name)

    if result is None:
        print("Unable to start the game.")
        return

    name, height, weight = result

    print("\nGuess the Pokemon!")
    print("Height:", height, "decimeters")
    print("Weight:", weight, "hectograms")

    print(" ")

    print("You have 3 attempts.")

    won = False

    for attempt in range(1, 4):
        guess = input("\nEnter Pokemon name: ").strip().lower()

        if guess == name:
            print("Correct! You guessed the Pokemon!")
            won = True
            break

        else:
            print("Wrong guess!")

    if won == False:
        print("\nYou ran out of attempts!")
        print("The correct Pokemon was:", name)

    print("\nThanks for playing!")


play_game()