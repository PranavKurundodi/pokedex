import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = tf.keras.models.load_model(
    "C:\\Users\\prana\\OneDrive\\Documents\\college\\pokedex\\backend\\model\\modelv4.h5"
)

# Define the target image size
target_size = (224, 224)
image = "C:\\Users\\prana\\OneDrive\\Documents\\college\\pokedex\\backend\\model\\pokemon.png"

# Load and preprocess the input image
input_image = load_img(image, target_size=target_size)
input_array = img_to_array(input_image) / 255.0
input_array = np.expand_dims(input_array, axis=0)

# Make the prediction
predictions = model.predict(input_array)

# Get the list of Pokemon names from the directory
pokemon_names = [
    "Abra",
    "Aerodactyl",
    "Alakazam",
    "Arbok",
    "Arcanine",
    "Articuno",
    "Beedrill",
    "Bellsprout",
    "Blastoise",
    "Bulbasaur",
    "Butterfree",
    "Caterpie",
    "Chansey",
    "Charizard",
    "Charmander",
    "Charmeleon",
    "Clefable",
    "Clefairy",
    "Cloyster",
    "Cubone",
    "Dewgong",
    "Diglett",
    "Ditto",
    "Dodrio",
    "Doduo",
    "Dragonair",
    "Dragonite",
    "Dratini",
    "Drowzee",
    "Dugtrio",
    "Eevee",
    "Ekans",
    "Electabuzz",
    "Electrode",
    "Exeggcute",
    "Exeggutor",
    "Farfetchd",
    "Fearow",
    "Flareon",
    "Gastly",
    "Gengar",
    "Geodude",
    "Gloom",
    "Golbat",
    "Goldeen",
    "Golduck",
    "Golem",
    "Graveler",
    "Grimer",
    "Growlithe",
    "Gyarados",
    "Haunter",
    "Hitmonchan",
    "Hitmonlee",
    "Horsea",
    "Hypno",
    "Ivysaur",
    "Jigglypuff",
    "Jolteon",
    "Jynx",
    "Kabuto",
    "Kabutops",
    "Kadabra",
    "Kakuna",
    "Kangaskhan",
    "Kingler",
    "Koffing",
    "Krabby",
    "Lapras",
    "Lickitung",
    "Machamp",
    "Machoke",
    "Machop",
    "Magikarp",
    "Magmar",
    "Magnemite",
    "Magneton",
    "Mankey",
    "Marowak",
    "Meowth",
    "Metapod",
    "Mew",
    "Mewtwo",
    "Moltres",
    "MrMime",
    "Muk",
    "Nidoking",
    "Nidoqueen",
    "Nidorina",
    "Nidorino",
    "Ninetales",
    "Oddish",
    "Omanyte",
    "Omastar",
    "Onix",
    "Paras",
    "Parasect",
    "Persian",
    "Pidgeot",
    "Pidgeotto",
    "Pidgey",
    "Pikachu",
    "Pinsir",
    "Poliwag",
    "Poliwhirl",
    "Poliwrath",
    "Ponyta",
    "Porygon",
    "Primeape",
    "Psyduck",
    "Raichu",
    "Rapidash",
    "Raticate",
    "Rattata",
    "Rhydon",
    "Rhyhorn",
    "Sandshrew",
    "Sandslash",
    "Scyther",
    "Seadra",
    "Seaking",
    "Seel",
    "Shellder",
    "Slowbro",
    "Slowpoke",
    "Snorlax",
    "Spearow",
    "Squirtle",
    "Starmie",
    "Staryu",
    "Tangela",
    "Tauros",
    "Tentacool",
    "Tentacruel",
    "Vaporeon",
    "Venomoth",
    "Venonat",
    "Venusaur",
    "Victreebel",
    "Vileplume",
    "Voltorb",
    "Vulpix",
    "Wartortle",
    "Weedle",
    "Weepinbell",
    "Weezing",
    "Wigglytuff",
    "Zapdos",
    "Zubat",
]

# Get the top 3 predictions
top_index = np.argmax(predictions[0])  # Get the index of the maximum probability
top_probability = predictions[0][top_index]  # Get the probability of the top prediction
top_pokemon = pokemon_names[top_index]  # Get the name of the top predicted Pokémon

# Print the results
print(top_pokemon)

