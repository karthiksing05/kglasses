import time
import datetime

import requests
from geopy.geocoders import Nominatim
import geocoder

from speech import pytts

def forecast(place):
    API_KEY = "e07645951fc23e5eff28bf74d9834912"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    completeURL = base_url + "appid=" + API_KEY + "&q=" + place

    response = requests.get(completeURL)
    json = response.json()

    if json["cod"] != "404":
        currTemp = 1.8 * (float(json["main"]["temp"]) - 273) + 32 # in kelvins, needs to be converted
        desc = json["weather"][0]["description"]
    
    else:
        raise Exception("City Not Found, please enter an acceptable city.")

    return currTemp, desc

def myLatLng():
    myloc = geocoder.ip('me')
    return myloc.latlng


def convertLatLngToLocation(lat, lng):
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Latitude & Longitude input 
    Latitude = lat
    Longitude = lng

    location = geolocator.reverse(str(Latitude) + "," + str(Longitude))

    address = location.raw['address']

    # traverse the data 
    city = address.get('city', '')

    return city


def get_weather(city):
    if city == "present":
        lat, lng = myLatLng()
        place = convertLatLngToLocation(lat, lng)
    else:
        place = city

    place = place.strip()

    temp, desc = forecast(place)

    return round(temp, 1), desc

if __name__ == "__main__":
    print(get_weather("present"))
