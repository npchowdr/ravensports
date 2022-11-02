from mimetypes import init
from sports.models import PlayerRegularSeasonTotals

class PerPossession:
    def __init__(self, totals: PlayerRegularSeasonTotals, num_poss=1):
        self.player = totals.playerId
        self.teamId = totals.teamId
        self.season = totals.season
        self.age = totals.age
        self.gamesPlayed = totals.gamesPlayed
        self.wins = totals.wins
        self.losses = totals.losses
        self.fgm = self.per_poss(stat=totals.fgm, possessions=totals.possessions, num_poss=num_poss)
        self.fga = self.per_poss(stat=totals.fga, possessions=totals.possessions, num_poss=num_poss)
        self.fgpct = totals.fgm / totals.fga
        self.fg3m = self.per_poss(stat=totals.fg3m, possessions=totals.possessions, num_poss=num_poss)
        self.fg3a = self.per_poss(stat=totals.fg3a, possessions=totals.possessions, num_poss=num_poss)
        self.fg3pct = totals.fg3m / totals.fg3a
        self.ftm = self.per_poss(stat=totals.ftm, possessions=totals.possessions, num_poss=num_poss)
        self.fta = self.per_poss(stat=totals.fta, possessions=totals.possessions, num_poss=num_poss)
        self.ftpct = totals.ftm / totals.fta
        self.offensiveRebounds = self.per_poss(totals.offensiveRebounds, totals.possessions, num_poss)
        self.defensiveRebounds = self.per_poss(totals.defensiveRebounds, totals.possessions, num_poss)
        self.rebounds = self.per_poss(stat=totals.rebounds, possessions=totals.possessions, num_poss=num_poss)
        self.assists = self.per_poss(stat=totals.assists, possessions=totals.possessions, num_poss=num_poss)
        self.turnovers = self.per_poss(stat=totals.turnovers, possessions=totals.possessions, num_poss=num_poss)
        self.steals = self.per_poss(stat=totals.steals, possessions=totals.possessions, num_poss=num_poss)
        self.blocks = self.per_poss(stat=totals.blocks, possessions=totals.possessions, num_poss=num_poss)
        self.blocks_against = self.per_poss(stat=totals.blocks_against, possessions=totals.possessions, num_poss=num_poss)
        self.personalFouls = self.per_poss(stat=totals.personalFouls, possessions=totals.possessions, num_poss=num_poss)
        self.personalFoulsDrawn = self.per_poss(totals.personalFoulsDrawn, totals.possessions, num_poss)
        self.points = self.per_poss(stat=totals.points, possessions=totals.possessions, num_poss=num_poss)


    def per_poss(stat, possessions, num_poss):
        return ((stat/possessions)*num_poss)