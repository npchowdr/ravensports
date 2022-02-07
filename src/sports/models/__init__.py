# __init__.py
import imp
from .team import Team
from .standings import Standings
#from .player import Player
from django.contrib import admin

# TODO admin.site register all Models
admin.site.register(Standings)  #test
admin.site.register(Team)
#admin.site.register(Player)