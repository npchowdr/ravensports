# __init__.py
import imp
from .team import Team
from .standings import Standings
from django.contrib import admin

# TODO admin.site register all Models
admin.site.register(Standings)
#admin.site.register(Team)
