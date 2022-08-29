from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('player_stats', views.player_stats, name='player_stats'),

]
