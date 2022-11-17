from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nba_home', views.nba_home, name='nba_home'),
    path('player_per_game_stats', views.player_per_game_stats, name='player_per_game_stats'),
    path('player_per_100_stats', views.player_per_100_stats, name='player_per_100_stats'),
    path('player_per_36_stats', views.player_per_36_stats, name='player_per_36_stats'),
    path('scatter_graph', views.scatter_graph, name='scatter_graph'),
    path('season_scatter_graph', views.season_scatter_graph, name='season_scatter_graph'),
    # path('season_scatter_graph_advanced', views.season_scatter_graph_advanced, name='season_scatter_graph_advanced'),
    path('api/get_all_players_regular_season_totals_stats_list', views.get_all_players_regular_season_totals_stats_list, name='get_all_players_regular_season_totals_stats_list'),
    path('api/get_player_regular_season_totals_stats_list/<str:player_slug>', views.get_player_regular_season_totals_stats_list, name='get_player_regular_season_totals_list'),
    path('api/get_players_stats_for_season_list/<str:season>', views.get_all_players_stats_for_season_list, name='get_all_players_stats_for_season_list'),
    #path('api/get_all_players_list', views.get_all_players_list, name='get_all_players_list'),
    #path('api/get_player_regular_season_per_game_stats_list/<str:player_slug>', views.get_player_regular_season_per_game_stats_list, name='get_player_regular_season_per_game_list'),
]
