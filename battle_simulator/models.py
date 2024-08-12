from django.db import models
import uuid

# Create your models here.

class Result:
    PLAYER1 = 1
    PLAYER2 = 2
    DRAW = 3

class BattleStatus:
    BATTLE_INPROGRESS = 1
    BATTLE_COMPLETED = 2
    BATTLE_FAILED = 3

class PokemonFightGame(models.Model):
    Result_choice = (
        (Result.PLAYER1, 'player1'),
        (Result.PLAYER2, 'player2'),
        (Result.DRAW, 'draw'),
        
    )
    
    BattleStatus_choice = (
        (BattleStatus.BATTLE_INPROGRESS, 'BATTLE_INPROGRESS'),
        (BattleStatus.BATTLE_COMPLETED, 'BATTLE_COMPLETED'),
        (BattleStatus.BATTLE_FAILED, 'BATTLE_FAILED'),
        
    )
    
    game_id = models.UUIDField(auto_created = True, unique=True, default = uuid.uuid4, editable = False)
    
    player1_pokemon = models.CharField(max_length=50, null=False, blank=False)
    player2_pokemon = models.CharField(max_length=50, null=False, blank=False)
    battle_status = models.SmallIntegerField(choices=BattleStatus_choice, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)
    margin = models.CharField(max_length=5, null=True, blank=True)
