from mimetypes import init
from typing import Dict
from sports.models import PlayerRegularSeasonTotals, Player, Team

class StatHelper:

    def get_percentage(makes, attempts):
        if makes == 0 or attempts == 0:
            return 0
        else:
            return round(makes/attempts * 100, 1)