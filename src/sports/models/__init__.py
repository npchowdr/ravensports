# __init__.py
import imp

import django.apps
from .team import Team
from django.contrib import admin
from .player import Player
from .player_regular_season_totals import PlayerRegularSeasonTotals


# TODO admin.site register all Models
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayerRegularSeasonTotals)


