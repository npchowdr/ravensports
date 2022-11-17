import imp
from rest_framework import serializers
from .models import *


class PlayerSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Player
        fields = [ 'playerLastName', 'playerFirstName', 'playerSlug', 'jerseyNumber', 'position',
                'height', 'weight', 'college', 'country', 'draftYear', 'draftRound', 'draftNumber',
                 'rosterStatus', 'fromYear', 'toYear']

class PlayerRegularSeasonTotalsSerializer(serializers.ModelSerializer):
    playerId = PlayerSerializer(many=False, read_only=True)
    class Meta:
        model = PlayerRegularSeasonTotals
        fields = ['id', 'season', 'age', 'possessions', 'gamesPlayed', 'wins', 'losses',
        'minutes','fgm', 'fga', 'fg3m', 'fg3a', 'ftm', 'fta', 'offensiveRebounds', 'defensiveRebounds',
        'rebounds', 'assists', 'turnovers', 'steals', 'blocks', 'blocks_against', 'personalFouls',
        'personalFoulsDrawn', 'points', 'plusMinus', 'doubleDoubles', 'tripleDoubles', 'playerId', 'teamId']


# class PlayerSeasonSerializer(serializers.ModelSerializer):
#     playerId = PlayerSerializer(many=False, read_only=True)
#     class Meta:
#         #model = PlayerSeason
#         fields = ['id', 'season', 'age', 'possessions', 'gamesPlayed', 'wins', 'losses',
#         'minutes','fgm', 'fga', 'fg3m', 'fg3a', 'ftm', 'fta', 'offensiveRebounds', 'defensiveRebounds',
#         'rebounds', 'assists', 'turnovers', 'steals', 'blocks', 'blocks_against', 'personalFouls',
#         'personalFoulsDrawn', 'points', 'plusMinus', 'doubleDoubles', 'tripleDoubles', 'playerId', 'teamId']