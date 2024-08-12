from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from battle_simulator.models import PokemonFightGame, BattleStatus
from base import response
from rest_framework import viewsets
from django.conf import settings
from pokemon_utils.pokemon import Pokemon
from base.pagination import PokemonSimulatorPagination
import json
from pokemon_utils.game import Game
from battle_simulator.task import fight_pokemon_player_taks

class PokemonBattleSimulatorViewSet(viewsets.ViewSet):
    
    model = PokemonFightGame
    permission_classes = [AllowAny]

    def get_queryset(self, phone):
        """
        Returns all the result
        """
        return self.model.objects.all()
        

    @action(detail=False, methods=['get'], url_path='pokemon-list')
    def pokemon_list(self, request, pk=None):
        if pk is None:
            pk = 1
        lis = [k for k, v in Pokemon.__dict__.items() if not k.startswith('__')]
        PokemonSimulatorPagination_obj = PokemonSimulatorPagination(lis, 10)
        page = PokemonSimulatorPagination_obj.page(pk)
        return response.Ok({
            'data' : page.object_list
        })
        
    
    
    @action(detail=False, methods=['post'], url_path='pokemon-fight')
    def pokemon_fight(self, request, pk=None):
        payload = json.loads(request.body)
        pokemon1 = payload.get('pokemon1')
        pokemon2 = payload.get('pokemon2')
        
        game_obj = Game(pokemon1, pokemon2)
        # model create object
        game_model_obj = PokemonFightGame.objects.create(
            player1_pokemon=pokemon1,
            player2_pokemon=pokemon2,
            battle_status = BattleStatus.BATTLE_INPROGRESS
        )
        # add in the celery
        fight_pokemon_player_taks.delay(game_obj, str(game_model_obj.game_id.hex))
        return response.Ok({
            'data' : str(game_model_obj.id)
        })
        
    
    @action(detail=False, methods=['get'], url_path='pokemon-fight-result')
    def pokemon_fight_result(self, request, pk=None):
        id = request.query_params.get('id')
        try:
            game_model_obj = PokemonFightGame.objects.get(game_id=id)
        except (PokemonFightGame.DoesNotExist, PokemonFightGame.MultipleObjectsReturned):
            response.BadRequest({
                'msg': 'Some Error, Try Again!'
            })
        
        return response.Ok({
        "status": dict(PokemonFightGame.BattleStatus_choice).get(game_model_obj.battle_status),
        "result": {
                    "winnerName": game_model_obj.result,
                    "wonByMargin": game_model_obj.margin
                    }
            })