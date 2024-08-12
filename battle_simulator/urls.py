from django.urls import path
from battle_simulator.api.routers import router as battle_simulator_router
from battle_simulator.api.viewsets import PokemonBattleSimulatorViewSet

urlpatterns = [
    path('simulator/pokemon-list/<int:pk>/', PokemonBattleSimulatorViewSet.as_view({'get': 'pokemon_list'})),
]

urlpatterns += battle_simulator_router.urls
