from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import datetime
from .models import PlayerPerGameStats, PlayerAdvancedStats, PlayerPer100Stats

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

def player_stats(request):
    # get all
    # all_per_game_stats = PlayerPerGameStats.objects.all()
    player = 'Kobe Bryant*'
    player_stats_object = PlayerPerGameStats.objects.filter(Player=player)  # HOFers have * next to name

    if request.method == "POST":
        searched = request.POST.get('searched')
        player = searched
        player_stats_object = PlayerPerGameStats.objects.filter(Player=searched)

        return render(request, 'table.html', {'player_stats_object': player_stats_object, 'player': player,
                                              'searched': searched})

    else: #default page render
        return render(request, 'table.html', {'player_stats_object': player_stats_object, 'player': player})





