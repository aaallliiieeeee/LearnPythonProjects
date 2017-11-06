import urllib2
import json

weather_api = 'a8b076330e2a1be4e475ffb7be833328'
weather = 'none'

url = 'http://samples.openweathermap.org/data/2.5/weather?zip=06037,us&appid=b1b15e88fa797225412429c1c50c122a1'


def weather_search(zipcode):
    api_key = weather_api
    zip_url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + str(zipcode) + ',us&appid=' + api_key
    json_obj = urllib2.urlopen(zip_url)

    data = json.load(json_obj)

    for item in data['weather']:
        weather = (item['main'])

    return "The weather forcast for today is", weather

zipcode = input("What is your locations zip code? ")
theWeather = weather_search(zipcode)
print theWeather




