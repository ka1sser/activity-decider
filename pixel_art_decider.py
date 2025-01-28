"""
This script will help me decide what to do, what to practice, and how to do it. I will start with 8x8, 16x16, then 32x32, and onwards.

I want this script to decide whether I will do the following:

1. What to draw = [objects, plants, animal, pokemon, anime character, or tv character]
2. Number of colors to use = [2, 4, 6, 8]
"""

import random
import logging
import json
from datetime import datetime
import time

def load_objects():
    with open("objects_list.json", "r") as file:
        config = json.load(file)
    
    listed = list(config)
    choices = random.sample(listed, k=3)
    return choices

def load_pokemons():
    with open("pokemons.json", "r") as file:
        config = json.load(file)
    
    listed = list(config)
    choices = random.sample(listed, k=3)
    return choices

def load_animals():
    with open("animals.json", "r") as file:
        config = json.load(file)
    
    listed = list(config)
    choices = random.sample(listed, k=3)
    return choices

def load_nature():
    with open("nature.json", "r") as file:
        config = json.load(file)
    
    listed = list(config)
    choices = random.sample(listed, k=3)
    return choices

def load_anime_char():
    with open("anime_chars.json", "r") as file:
        config = json.load(file)
    
    listed = list(config)
    choices = random.sample(listed, k=3)
    return choices

def load_tv_char():
    with open("tv_chars.json", "r") as file:
        config = json.load(file)
    
    listed = list(config)
    choices = random.sample(listed, k=3)
    return choices

def load_four_color_palette():
    with open("four_color_palette.json", "r") as file:
        config = json.load(file)
    
    listed = list(config)
    choice = random.sample(listed)
    return choice

def main():
    logging.basicConfig(
        filename="pixel_art_decider.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s : %(message)s"
    )

    current_time = datetime.now()
    current_time = current_time.strftime("%B %d, %Y")
    categories = ["object", "pokemon", "animal", "nature", "anime_char", "tv_char"]

    choice_in_categories = random.choice(categories)
    
    logging.info("Hey, I am the task master.")
    logging.info(f"Today is {current_time}")
    logging.info(f"I have chosen this category: {choice_in_categories.title()}")

    match choice_in_categories:
        case "object":
            objects = load_objects()
            logging.info(f"Create pixel art for the following: {objects}")
        case "pokemon":
            pokemons = load_pokemons()
            logging.info(f"Create pixel art for the following: {pokemons}")
        case "animal":
            animals = load_animals()
            logging.info(f"Create pixel art for the following: {animals}")
        case "nature":
            nature = load_nature()
            logging.info(f"Create pixel art for the following: {nature}")
        case "anime_char":
            anime_chars = load_anime_char()
            logging.info(f"Create pixel art for the following: {anime_chars}")
        case "tv_char":
            tv_chars = load_tv_char()
            logging.info(f"Create pixel art for the following: {tv_chars}")

    random_four_color_palette = load_four_color_palette()
    logging.info(f"You are allowed to use the color palette: {random_four_color_palette}")
    logging.info("MOVE!\n")
    
if __name__ == "__main__":
    main()