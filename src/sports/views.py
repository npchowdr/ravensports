from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import datetime

import datetime

now = datetime.datetime.now()

def home(request):

#api request
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
    
    return render(request,'index.html',{'api':api})




