from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('player_per_game_stats', views.player_per_game_stats, name='player_per_game_stats'),
    path('player_per_100_stats', views.player_per_100_stats, name='player_per_100_stats'),
    path('player_advanced_stats', views.player_advanced_stats, name='player_advanced_stats'),
    path('scatter_graph', views.scatter_graph, name='scatter_graph'),
    path('api/get_all_players_per_game_stats_list', views.get_all_players_per_game_stats_list, name='get_all_players_per_game_stats_list'),
    path('api/get_player_per_game_stats_list/<str:player>', views.get_player_per_game_stats_list, name='get_player_ger_stats_list'),
]
