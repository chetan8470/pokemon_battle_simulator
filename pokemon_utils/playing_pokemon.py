import pandas as pd
from pokemon_utils.pokemon import Pokemon
from django.conf import settings
import os

class PlayingPokemon:
    def __init__(self, name) -> None:
        self.pokemon_name = name
        self.type1 = None
        self.type2 = None
        self.attack = None

    @staticmethod
    def get_csv_file_obj():
        path = os.path.join(settings.BASE_DIR, 'pokemon.csv')
        df = pd.read_csv(path)
        return df
    
    @staticmethod
    def get_pokemon_csv_index(pokemon_name):
        for k, v in Pokemon.__dict__.items():
            if not k.startswith('__') and k == pokemon_name:
                return v
        return -1
    
    def setter(self):
        df = PlayingPokemon.get_csv_file_obj()
        pokemon_idx = PlayingPokemon.get_pokemon_csv_index(self.pokemon_name)
        pokemon_data = df.iloc[pokemon_idx]
        self.type1 = int(pokemon_data.get('against_grass'))
        self.type2 = int(pokemon_data.get('against_poison'))
        self.attack = int(pokemon_data.get('attack'))
        return
    
    
class Player(PlayingPokemon):
    def __init__(self, name):
        PlayingPokemon.__init__(self, name)

    def set_pokemon_val(self):
        super().setter() 
        return

