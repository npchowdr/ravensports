from mimetypes import init
from typing import Dict
from sports.models import PlayerRegularSeasonTotals, Player, Team

class StatHelper:

    def get_percentage(makes, attempts):
        if makes == 0 or attempts == 0:
            return 0
        else:
            return round(makes/attempts * 100, 1)

    def missed_fg_possessions(fgm, fga, team_orb_pct):
        return (fga - fgm) * (1 - 1.07 + team_orb_pct)

    def missed_ft_possessions(ftm, fta):
        return pow(((1 - (ftm/fta))), 2) * 0.4 * fta