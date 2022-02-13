from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models.player_per_game_stats import PlayerPerGameStats

import requests
import json
import datetime

import datetime

now = datetime.datetime.now()


def home(request):
    # api request
    today_date = datetime.date.today()
    url = "https://api-nba-v1.p.rapidapi.com/games/date/{}".format(today_date)

    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "17c670de23mshfd6cbf40f8dcb0ap1d1114jsn76ac1068f254"
    }

    api_request = requests.get(url, headers=headers)

    try:
        api = json.loads(api_request.content)
    except:
        api = "Error..."

    #TODO - query db for player data
    player_per_game = PlayerPerGameStats.objects.all()

    #return render(request, 'index.html', {'api': api}) #, {'player_per_game': player_per_game}
    return  render(request, 'index.html', {'player_per_game': player_per_game})
