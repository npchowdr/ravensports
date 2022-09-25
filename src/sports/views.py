from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
import datetime
from .models import PlayerPerGameStats, PlayerAdvancedStats, PlayerPer100Stats
from .serializers import PlayerPerGameStatsSerializer, PlayerAdvancedStatsSerializer
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
    player = 'Kobe Bryant*'
    player_stats_object = PlayerPerGameStats.objects.filter(Player=player)  # HOFers have * next to name

    if request.method == "POST":
        searched = request.POST.get('searched')
        player_stats_object = PlayerPerGameStats.objects.filter(Player=searched)

        return render(request, 'table.html', {'player_stats_object': player_stats_object, 'player': searched,
                                              'searched': searched})

    else:
        return render(request, 'table.html', {'player_stats_object': player_stats_object, 'player': player})

# -------------------
def player_per_100_stats(request):
    player = 'Kobe Bryant*'
    player_stats_object = PlayerPer100Stats.objects.filter(Player=player)  # HOFers have * next to name

    if request.method == "POST":
        searched = request.POST.get('searched')
        player_stats_object = PlayerPer100Stats.objects.filter(Player=searched)

        return render(request, 'player_per_100_table.html', {'player_stats_object': player_stats_object,
                                                             'player': searched, 'searched': searched})

    else:
        return render(request, 'player_per_100_table.html', {'player_stats_object': player_stats_object,
                                                             'player': player})

# -------------------
def player_advanced_stats(request):
    player = 'Kobe Bryant*'
    player_stats_object = PlayerAdvancedStats.objects.filter(Player=player)  # HOFers have * next to name

    if request.method == "POST":
        searched = request.POST.get('searched')
        player_stats_object = PlayerAdvancedStats.objects.filter(Player=searched)

        return render(request, 'player_advanced_table.html', {'player_stats_object': player_stats_object,
                                                             'player': searched, 'searched': searched})

    else:
        return render(request, 'player_advanced_table.html', {'player_stats_object': player_stats_object,
                                                             'player': player})

# -------------------
def scatter_graph(request):
    player = 'Anthony Davis'

    if request.method == "POST":
        searched = request.POST.get('searched')
        return render(request, 'scatter_graph.html', {'player': searched, 'searched': searched})
    else:
        return render(request, 'scatter_graph.html', {'player': player})

# -------------------
def season_scatter_graph(request):
    season = 2021

    if request.method == "POST":
        searched = request.POST.get('searched')
        return render(request, 'season_scatter_graph.html', {'season': searched, 'searched': searched})
    else:
        return render(request, 'season_scatter_graph.html', {'season': season})

# -------------------
def get_all_players_per_game_stats_list(request):
    try:
        player_per_game_objects = PlayerPerGameStats.objects.all()
    except PlayerPerGameStats.DoesNotExist:
        return HttpResponse(status=404)

    serializer = PlayerPerGameStatsSerializer(player_per_game_objects, many=True)

    return JsonResponse(serializer.data, safe=False)

# -------------------
def get_player_per_game_stats_list(request, player='Kobe Bryant*'):
    player_per_game_objects = PlayerPerGameStats.objects.filter(Player=player)
    serializer = PlayerPerGameStatsSerializer(player_per_game_objects, many=True)
    return JsonResponse({'player_per_game_stats': serializer.data})

# -------------------
# @param stats_type can be 'advanced', 'per game', or 'per 100'
def get_all_players_stats_for_season_list(request, season=2021):

    player_advanced_stats_object = PlayerAdvancedStats.objects.filter(Year=season)
    player_per_game_stats_object = PlayerPerGameStats.objects.filter(Year=season)
    per_game_serializer = PlayerPerGameStatsSerializer(player_per_game_stats_object, many=True)
    advanced_serializer = PlayerAdvancedStatsSerializer(player_advanced_stats_object, many=True)

    return JsonResponse({'player_per_game_stats': per_game_serializer.data,
                        'player_advanced_stats': advanced_serializer.data})
       
   
    
    