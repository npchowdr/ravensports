from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('player_per_game_stats', views.player_per_game_stats, name='player_per_game_stats'),
    path('player_per_100_stats', views.player_per_100_stats, name='player_per_100_stats'),
]
