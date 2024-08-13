from celery import shared_task
from battle_simulator.models import PokemonFightGame, BattleStatus
from pokemon_utils.game import Game


@shared_task
def fight_pokemon_player_taks(pokemon1, pokemon2, id):
    try:
        game_model_obj = PokemonFightGame.objects.get(game_id=id)
        g = Game(pokemon1, pokemon2)
        g.startGame()
        result, score =  g.fight_result()
        game_model_obj.result = result
        game_model_obj.margin = score
        game_model_obj.battle_status = BattleStatus.BATTLE_COMPLETED
        game_model_obj.save()
    except (PokemonFightGame.DoesNotExist, PokemonFightGame.MultipleObjectsReturned):
        pass
    except Exception as e:
        game_model_obj.battle_status = BattleStatus.BATTLE_FAILED
        game_model_obj.save()
    return 

