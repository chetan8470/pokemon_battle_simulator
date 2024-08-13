from django.contrib import admin
from battle_simulator.models import PokemonFightGame

# Register your models here.

class PokemonFightGameAdmin(admin.ModelAdmin):
    list_display = ( 'game_id',  'player1_pokemon',  'player2_pokemon',  'battle_status', 'result', 'margin')
    readonly_fields = ['game_id']

admin.site.register(PokemonFightGame, PokemonFightGameAdmin)
