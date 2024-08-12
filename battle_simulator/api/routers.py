from rest_framework.routers import DefaultRouter
from battle_simulator.api.viewsets import PokemonBattleSimulatorViewSet

router = DefaultRouter()

router.register(r"simulator", PokemonBattleSimulatorViewSet, basename="PokemonBattleSimulator")

