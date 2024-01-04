import requests

def getweather(city):
    url = f'https://es.wttr.in/{city}?format=j1'
    response = requests.get(url)
    weather_dic = response.json()
    print(weather_dic['current_condition'][0]['FeelsLikeC'])

getweather('chicago')