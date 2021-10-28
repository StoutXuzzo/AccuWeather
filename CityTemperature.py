import requests, json, urllib3

urllib3.disable_warnings()

global apikey
apikey = "Ftk2nOMhCvKGR10QPbmYs6cYjxgd83za"

def getCityInfo(cityName):
    url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    response = requests.request("GET", url + "?apikey=" + apikey + "&q=" + cityName, verify = False)
    cityInfo = json.loads(response.content)
    return cityInfo[0]

def getCityWeather(cityKey):
    url = "http://dataservice.accuweather.com/currentconditions/v1/" + cityKey
    response = requests.request("GET", url + "?apikey=" + apikey, verify = False)
    cityWeather = json.loads(response.content)
    return cityWeather[0]

while True:
    user = input("Input a city name or 'exit' to close: ")

    if user.upper() == "EXIT":
        break

    city = getCityInfo(user)
    key = city["Key"]
    weather = getCityWeather(key)

    print("\n" + city["EnglishName"] + ":")
    print("   Weather: " + weather["WeatherText"])

    if weather["HasPrecipitation"]:
        print("   Precipitation: " + weather["PrecipitationType"])
    else:
        print("   Precipitation: No")

    print("   Temperature: " + str(weather["Temperature"]["Metric"]["Value"]), end="")
    print(weather["Temperature"]["Metric"]["Unit"], end="")
    print("  /  " + str(weather["Temperature"]["Imperial"]["Value"]), end="")
    print(weather["Temperature"]["Imperial"]["Unit"])
    print("")

