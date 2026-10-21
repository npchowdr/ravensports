from mimetypes import init
from typing import Dict
from sports.models import PlayerRegularSeasonTotals, Player, Team
from .stat_helper import StatHelper

class PerMinute:
    def __init__(self, totals: PlayerRegularSeasonTotals):
        self.player = totals.playerId
        self.teamId = totals.teamId
        self.season = totals.season
        self.age = totals.age
        self.gamesPlayed = totals.gamesPlayed
        self.possessions = self.per_minute(stat=totals.possessions, minutes=totals.minutes)
        self.wins = totals.wins
        self.losses = totals.losses
        self.minutes = self.per_minute(stat=totals.minutes, minutes=totals.minutes)
        self.fgm = self.per_minute(stat=totals.fgm, minutes=totals.minutes)
        self.fga = self.per_minute(stat=totals.fga, minutes=totals.minutes)
        self.fgpct = totals.fgm / totals.fga
        self.fg3m = self.per_minute(stat=totals.fg3m, minutes=totals.minutes)
        self.fg3a = self.per_minute(stat=totals.fg3a, minutes=totals.minutes)
        self.fg3pct = totals.fg3m / totals.fg3a
        self.ftm = self.per_minute(stat=totals.ftm, minutes=totals.minutes)
        self.fta = self.per_minute(stat=totals.fta, minutes=totals.minutes)
        self.ftpct = totals.ftm / totals.fta
        self.offensiveRebounds = self.per_minute(stat=totals.offensiveRebounds, minutes=totals.minutes)
        self.defensiveRebounds = self.per_minute(stat=totals.defensiveRebounds, minutes=totals.minutes)
        self.rebounds = self.per_minute(stat=totals.rebounds, minutes=totals.minutes)
        self.assists = self.per_minute(stat=totals.assists, minutes=totals.minutes)
        self.turnovers = self.per_minute(stat=totals.turnovers, minutes=totals.minutes)
        self.steals = self.per_minute(stat=totals.steals, minutes=totals.minutes)
        self.blocks = self.per_minute(stat=totals.blocks, minutes=totals.minutes)
        self.blocks_against = self.per_minute(stat=totals.blocks_against, minutes=totals.minutes)
        self.personalFouls = self.per_minute(stat=totals.personalFouls, minutes=totals.minutes)
        self.personalFoulsDrawn = self.per_minute(stat=totals.personalFoulsDrawn, minutes=totals.minutes)
        self.points = self.per_minute(stat=totals.points, minutes=totals.minutes)
        self.plusMinus = self.per_minute(stat=totals.points, minutes=totals.minutes)

    def __init__(self, totals: Dict, mins=1):
        self.player = totals['playerId_id']
        self.teamId = Team.objects.filter(id=totals['teamId_id']).get().abbreviation
        self.season = totals['season']
        self.age = totals['age']
        self.gamesPlayed = totals['gamesPlayed']
        self.wins = totals['wins']
        self.losses = totals['losses']
        self.fgm = self.per_minute(stat=totals['fgm'], minutes=totals['minutes'], per_mins=mins)
        self.fga = self.per_minute(stat=totals['fga'], minutes=totals['minutes'], per_mins=mins)
        self.fgpct = StatHelper.get_percentage(totals['fgm'], totals['fga'])
        self.fg3m = self.per_minute(stat=totals['fg3m'], minutes=totals['minutes'], per_mins=mins)
        self.fg3a = self.per_minute(stat=totals['fg3a'], minutes=totals['minutes'], per_mins=mins)
        self.fg3pct = StatHelper.get_percentage(totals['fg3m'], totals['fg3a'])
        self.ftm = self.per_minute(stat=totals['ftm'], minutes=totals['minutes'], per_mins=mins)
        self.fta = self.per_minute(stat=totals['fta'], minutes=totals['minutes'], per_mins=mins)
        self.ftpct = StatHelper.get_percentage(totals['ftm'], totals['fta'])
        self.offensiveRebounds = self.per_minute(stat=totals['offensiveRebounds'], minutes=totals['minutes'], per_mins=mins)
        self.defensiveRebounds = self.per_minute(stat=totals['defensiveRebounds'], minutes=totals['minutes'], per_mins=mins)
        self.rebounds = self.per_minute(stat=totals['rebounds'], minutes=totals['minutes'], per_mins=mins)
        self.assists = self.per_minute(stat=totals['assists'], minutes=totals['minutes'], per_mins=mins)
        self.turnovers = self.per_minute(stat=totals['turnovers'], minutes=totals['minutes'], per_mins=mins)
        self.steals = self.per_minute(stat=totals['steals'], minutes=totals['minutes'], per_mins=mins)
        self.blocks = self.per_minute(stat=totals['blocks'], minutes=totals['minutes'], per_mins=mins)
        self.blocks_against = self.per_minute(stat=totals['blocks_against'], minutes=totals['minutes'], per_mins=mins)
        self.personalFouls = self.per_minute(stat=totals['personalFouls'], minutes=totals['minutes'], per_mins=mins)
        self.personalFoulsDrawn = self.per_minute(stat=totals['personalFoulsDrawn'], minutes=totals['minutes'], per_mins=mins)
        self.points = self.per_minute(stat=totals['points'], minutes=totals['minutes'], per_mins=mins)
        self.plusMinus = self.per_minute(stat=totals['plusMinus'], minutes=totals['minutes'], per_mins=mins)

    def per_minute(self, stat, minutes, per_mins):
        return round((stat/minutes) * per_mins, 1) 