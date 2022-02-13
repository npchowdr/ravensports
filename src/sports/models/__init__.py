# __init__.py
import imp
from .team import Team
from .standings import Standings
from .player_per_game_stats import PlayerPerGameStats
from django.contrib import admin

# TODO admin.site register all Models
admin.site.register(Standings)  #test
admin.site.register(Team)
admin.site.register(PlayerPerGameStats)