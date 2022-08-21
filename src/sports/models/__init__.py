# __init__.py
import imp

import django.apps
from .team import Team
from .standings import Standings
from django.contrib import admin
from .player_per_game_stats import PlayerPerGameStats
from .player_per_100_stats import PlayerPer100Stats
from .player_advanced_stats import PlayerAdvancedStats
from .playoff_player_advanced_stats import PlayoffPlayerAdvancedStats


# TODO admin.site register all Models
admin.site.register(Standings)
admin.site.register(Team)
admin.site.register(PlayerPerGameStats)
admin.site.register(PlayerPer100Stats)
admin.site.register(PlayerAdvancedStats)
admin.site.register(PlayoffPlayerAdvancedStats)


