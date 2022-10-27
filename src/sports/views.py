from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
import datetime
from .models import *
from .serializers import *
from .stats.per_game import PerGame
from .stats.per_minute import PerMinute
from rest_framework.decorators import api_view

def home(request):
    #api request
    #today_date = datetime.date.today()
    #url = "https://api-nba-v1.p.rapidapi.com/games/date/{}".format(today_date)
    url = "https://free-nba.p.rapidapi.com/games"

    headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "30c951b069msh648c965fd6a0c86p1f0812jsnc4bc8a94668d"
    }

    api_request = requests.get(url, headers=headers)
    #response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        api = json.loads(api_request.content)
    except:
        api = "Error..."

    return render(request, 'index.html', {'api': api})

# -------------------
def player_per_game_stats(request):
    # get all
    # all_per_game_stats = PlayerPerGameStats.objects.all()
    player = 'Kobe Bryant'
    playerSlug = 'kobe-bryant'

    player_object = Player.objects.filter(playerSlug=playerSlug).get()
    #player_stats_object = PlayerRegularSeasonTotals.objects.filter(playerId=2)
    player_stats_object = PlayerRegularSeasonTotals.objects.filter(playerId=player_object.id)

    stat_list = []

    for player_season in player_stats_object.values():
        #per_game_stats = player_season
        per_game_stats = PerGame(player_season)
        stat_list.append(per_game_stats)

    if request.method == "POST":
        searched = request.POST.get('searched')
        player_stats_object = PlayerRegularSeasonTotals.objects.filter(playerId=player_object.id)
 
        return render(request, 'table.html', {'player_stats_object': player_stats_object, 'player': searched,
                                              'searched': searched, 'player_obj': player_object})

    else:
        return render(request, 'table.html', {'player_stats_object': player_stats_object, 'player': player, 
        'player_obj': player_object, 'stat_list': stat_list})

# -------------------
# def player_per_100_stats(request):
#     player = 'Kobe Bryant*'
#     player_stats_object = PlayerPer100Stats.objects.filter(Player=player)  # HOFers have * next to name

#     if request.method == "POST":
#         searched = request.POST.get('searched')
#         player_stats_object = PlayerPer100Stats.objects.filter(Player=searched)

#         return render(request, 'player_per_100_table.html', {'player_stats_object': player_stats_object,
#                                                              'player': searched, 'searched': searched})

#     else:
#         return render(request, 'player_per_100_table.html', {'player_stats_object': player_stats_object,
#                                                              'player': player})

# # -------------------
# def player_advanced_stats(request):
#     player = 'Kobe Bryant*'
#     player_stats_object = PlayerAdvancedStats.objects.filter(Player=player)  # HOFers have * next to name

#     if request.method == "POST":
#         searched = request.POST.get('searched')
#         player_stats_object = PlayerAdvancedStats.objects.filter(Player=searched)

#         return render(request, 'player_advanced_table.html', {'player_stats_object': player_stats_object,
#                                                              'player': searched, 'searched': searched})

#     else:
#         return render(request, 'player_advanced_table.html', {'player_stats_object': player_stats_object,
#                                                              'player': player})

# -------------------
# def scatter_graph(request):
#     player = 'Anthony Davis'

#     if request.method == "POST":
#         searched = request.POST.get('searched')
#         return render(request, 'scatter_graph.html', {'player': searched, 'searched': searched})
#     else:
#         return render(request, 'scatter_graph.html', {'player': player})

# # -------------------
# def season_scatter_graph(request):
#     season = 2021

#     if request.method == "POST":
#         searched = request.POST.get('searched')
#         return render(request, 'season_scatter_graph.html', {'season': searched, 'searched': searched})
#     else:
#         return render(request, 'season_scatter_graph.html', {'season': season})

# # -------------------
# def season_scatter_graph_advanced(request):
#     season = 2021

#     if request.method == "POST":
#         searched = request.POST.get('searched')
#         return render(request, 'season_scatter_graph_advanced.html', {'season': searched, 'searched': searched})
#     else:
#         return render(request, 'season_scatter_graph_advanced.html', {'season': season})

# -------------------
# def get_all_players_per_game_stats_list(request):
    # try:
    #     player_per_game_objects = PlayerPerGameStats.objects.all()
    # except PlayerPerGameStats.DoesNotExist:
    #     return HttpResponse(status=404)

    # serializer = PlayerPerGameStatsSerializer(player_per_game_objects, many=True)

    # return JsonResponse(serializer.data, safe=False)

# -------------------
# def get_player_per_game_stats_list(request, player='Kobe Bryant*'):
#     player_per_game_objects = PlayerPerGameStats.objects.filter(Player=player)
#     serializer = PlayerPerGameStatsSerializer(player_per_game_objects, many=True)
#     return JsonResponse({'player_per_game_stats': serializer.data})

# # -------------------
# # @param stats_type can be 'advanced', 'per game', or 'per 100'
# def get_all_players_stats_for_season_list(request, season=2021):
#     player_advanced_stats_object = PlayerAdvancedStats.objects.filter(Year=season)
#     player_per_game_stats_object = PlayerPerGameStats.objects.filter(Year=season)
#     per_game_serializer = PlayerPerGameStatsSerializer(player_per_game_stats_object, many=True)
#     advanced_serializer = PlayerAdvancedStatsSerializer(player_advanced_stats_object, many=True)

#     return JsonResponse({'player_per_game_stats': per_game_serializer.data,
#                         'player_advanced_stats': advanced_serializer.data})
       
# -------------------
# def get_player_regular_season_totals(request, season='2021-22'):
#     player_total_stats = PlayerRegularSeasonTotals.objects.filter(season=season)
#     player_total_serializer = PlayerRegularSeasonTotalsSerializer(player_total_stats, many=True)
    
#     return JsonResponse({'regular_season_totals': player_total_serializer.data})

