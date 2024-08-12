from pokemon_utils.playing_pokemon import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)

    def (self):
        self.player1.set_pokemon_val()
        self.player2.set_pokemon_val()
        return

    def (self):
        damage1 = (self.player1.attack / 200) *100 -((self.player2.type1 / 4)*100 + (self.player2.type1 / 4)*100)
        return damage1
    
    
    def (self):
        damage2 = (self.player2.attack / 200) *100 -((self.player1.type1 / 4)*100 + (self.player1.type1 / 4)*100)
        return damage2
    
    def (self):
        damage1 = self.pokemon_fight1()
        damage2 = self.pokemon_fight2()
        if damage1 > damage2 :
            return self.player2.pokemon_name, damage1-damage2
        elif damage1 < damage2 :
            return self.player1.pokemon_name, damage2-damage1
        else:
            return 'draw', 0