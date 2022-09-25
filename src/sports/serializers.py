import imp
from rest_framework import serializers
from .models import PlayerPerGameStats
from .models import PlayerPer100Stats
from .models import PlayerAdvancedStats

class PlayerPerGameStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPerGameStats
        fields = ['id', 'Rank', 'Player', 'Position', 'Age', 'Team', 'GamesPlayed', 'GamesStarted',
        'MinutesPlayed', 'FieldGoalsMade', 'FieldGoalsAttempted', 'FieldGoalPercentage', 'ThreePointersMade',
        'ThreePointersAttempted', 'ThreePointPercentage', 'TwoPointersMade', 'TwoPointersAttempted',
        'TwoPointPercentage', 'EffectiveFieldGoalPercentage', 'FreeThrowsMade', 'FreeThrowsAttempted',
        'FreeThrowPercentage', 'OffensiveRebounds', 'DefensiveRebounds', 'TotalRebounds', 'Assists',
        'Steals', 'Blocks', 'Turnovers', 'PersonalFouls', 'Points', 'Year']

    def get_stats(self, data):
        return PlayerPerGameStats.objects.all()


class PlayerAdvancedStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAdvancedStats
        fields = ['id', 'Rank', 'Player', 'Position', 'Age', 'Team', 'GamesPlayed', 'MinutesPlayed',
        'PlayerEfficiencyRating', 'TrueShootingPercentage', 'ThreePointAttemptRate', 'FreeThrowAttemptRate',
        'OffensiveReboundPercentage', 'DefensiveReboundPercentage', 'TotalReboundPercentage', 'AssistPercentage',
        'StealPercentage', 'BlockPercentage', 'TurnoverPercentage', 'UsagePercentage', 'OffensiveWinShares',
        'DefensiveWinShares', 'WinShares', 'WinSharesPer48', 'OffensiveBoxPlusMinus', 'DefensiveBoxPlusMinus',
        'ValueOverReplacementPlayer', 'Year']

    def get_stats(self, data):
        return PlayerAdvancedStats.objects.all()
