import imp
from rest_framework import serializers
from .models import *


class PlayerRegularSeasonTotalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRegularSeasonTotals
        fields = ['id', 'season', 'age', 'possessions', 'gamesPlayed', 'wins', 'losses',
        'minutes','fgm', 'fga', 'fg3m', 'fg3a', 'ftm', 'fta', 'offensiveRebounds', 'defensiveRebounds',
        'rebounds', 'assists', 'turnovers', 'steals', 'blocks', 'blocksAgainst', 'personalFouls',
        'personalFoulsDrawn', 'points', 'plusMinus', 'doubleDoubles', 'tripleDoubles', 'playerId', 'teamId']


