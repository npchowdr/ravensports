from mimetypes import init
from typing import Dict
from sports.models import PlayerRegularSeasonTotals, Player, Team
from .stat_helper import StatHelper

class PerGame:

    def __init__(self, totals: PlayerRegularSeasonTotals):
        self.player = totals.playerId
        self.teamId = totals.teamId
        self.season = totals.season
        self.age = totals.age
        self.gamesPlayed = totals.gamesPlayed
        self.possessions = self.per_game(stat=totals.possessions, games=totals.gamesPlayed)
        self.wins = totals.wins
        self.losses = totals.losses
        self.minutes = self.per_game(stat=totals.minutes, games=totals.gamesPlayed)
        self.fgm = self.per_game(stat=totals.fgm, games=totals.gamesPlayed)
        self.fga = self.per_game(stat=totals.fga, games=totals.gamesPlayed)
        self.fgpct = StatHelper.get_percentage(totals.fgm,totals.fga)
        self.fg3m = self.per_game(stat=totals.fg3m, games=totals.gamesPlayed)
        self.fg3a = self.per_game(stat=totals.fg3a, games=totals.gamesPlayed)
        self.fg3pct = StatHelper.get_percentage(totals.fg3m, totals.fg3a)
        self.ftm = self.per_game(stat=totals.ftm, games=totals.gamesPlayed)
        self.fta = self.per_game(stat=totals.fta, games=totals.gamesPlayed)
        self.ftpct = StatHelper.get_percentage(totals.ftm,totals.fta)
        self.offensiveRebounds = self.per_game(stat=totals.offensiveRebounds, games=totals.gamesPlayed)
        self.defensiveRebounds = self.per_game(stat=totals.defensiveRebounds, games=totals.gamesPlayed)
        self.rebounds = self.per_game(stat=totals.rebounds, games=totals.gamesPlayed)
        self.assists = self.per_game(stat=totals.assists, games=totals.gamesPlayed)
        self.turnovers = self.per_game(stat=totals.turnovers, games=totals.gamesPlayed)
        self.steals = self.per_game(stat=totals.steals, games=totals.gamesPlayed)
        self.blocks = self.per_game(stat=totals.blocks, games=totals.gamesPlayed)
        self.blocks_against = self.per_game(stat=totals.blocks_against, games=totals.gamesPlayed)
        self.personalFouls = self.per_game(stat=totals.personalFouls, games=totals.gamesPlayed)
        self.personalFoulsDrawn = self.per_game(stat=totals.personalFoulsDrawn, games=totals.gamesPlayed)
        self.points = self.per_game(stat=totals.points, games=totals.gamesPlayed)
        self.plusMinus = self.per_game(stat=totals.points, games=totals.gamesPlayed)

    def __init__(self, totals: Dict):
        self.player = totals['playerId_id']
        self.teamId = Team.objects.filter(id=totals['teamId_id']).get().abbreviation
        self.season = totals['season']
        self.age = totals['age']
        self.gamesPlayed = totals['gamesPlayed']
        self.possessions = self.per_game(totals['possessions'], totals['gamesPlayed'])
        self.wins = totals['wins']
        self.losses = totals['losses']
        self.minutes = self.per_game(stat=totals['minutes'], games=totals['gamesPlayed'])
        self.fgm = self.per_game(stat=totals['fgm'], games=totals['gamesPlayed'])
        self.fga = self.per_game(stat=totals['fga'], games=totals['gamesPlayed'])
        self.fgpct = StatHelper.get_percentage(totals['fgm'], totals['fga'])
        self.fg3m = self.per_game(stat=totals['fg3m'], games=totals['gamesPlayed'])
        self.fg3a = self.per_game(stat=totals['fg3a'], games=totals['gamesPlayed'])
        self.fg3pct = StatHelper.get_percentage(totals['fg3m'], totals['fg3a'])
        self.ftm = self.per_game(stat=totals['ftm'], games=totals['gamesPlayed'])
        self.fta = self.per_game(stat=totals['fta'], games=totals['gamesPlayed'])
        self.ftpct = StatHelper.get_percentage(totals['ftm'], totals['fta'])
        self.offensiveRebounds = self.per_game(stat=totals['offensiveRebounds'], games=totals['gamesPlayed'])
        self.defensiveRebounds = self.per_game(stat=totals['defensiveRebounds'], games=totals['gamesPlayed'])
        self.rebounds = self.per_game(stat=totals['rebounds'], games=totals['gamesPlayed'])
        self.assists = self.per_game(stat=totals['assists'], games=totals['gamesPlayed'])
        self.turnovers = self.per_game(stat=totals['turnovers'], games=totals['gamesPlayed'])
        self.steals = self.per_game(stat=totals['steals'], games=totals['gamesPlayed'])
        self.blocks = self.per_game(stat=totals['blocks'], games=totals['gamesPlayed'])
        self.blocks_against = self.per_game(stat=totals['blocks_against'], games=totals['gamesPlayed'])
        self.personalFouls = self.per_game(stat=totals['personalFouls'], games=totals['gamesPlayed'])
        self.personalFoulsDrawn = self.per_game(stat=totals['personalFoulsDrawn'], games=totals['gamesPlayed'])
        self.points = self.per_game(stat=totals['points'], games=totals['gamesPlayed'])
        self.plusMinus = self.per_game(stat=totals['plusMinus'], games=totals['gamesPlayed'])


    def per_game(self, stat, games):
        return round(stat/games, 2)
