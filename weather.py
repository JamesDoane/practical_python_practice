import requests

api_key = '350a1e81b2c78c5d8b90c1fa9b91c716'



def get_weather():
    city = input("Enter a city: ")
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    
    
    print("today's forecast is", description)
    print("the low for today is",temp_min,end=" ")
    print("and the high will be", temp_max)
    
get_weather()