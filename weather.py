import requests
import geocoder

def get_weather(city):

    if city == "present":
        g = list(geocoder.ip('me'))
        g = list(g)[0]
        city = g

    API_KEY = "d02bb3d0fbb7ac7c6b2e52f5d1a37bf6"
    r = requests.get(f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}&units=f")
    if r:
        data = r.json()
        temperature = data["current"]["temperature"]
        feelsLike = data["current"]["feelslike"]
        precip = data["current"]["precip"]
        desc = list(data["current"]["weather_descriptions"])

        finalStr = f"Today in {city} it is "
        i = 0
        for x in desc:
            finalStr += x
            i += 1
            if i != len(desc):
                finalStr += " and "
        
        finalStr += f". The temperature is {temperature} but it feels like {feelsLike}. There is a precipitation of {precip}."

        return finalStr

    else:
        print("request failed :(")
        return ""

if __name__ == "__main__":
    print(get_weather("antartica"))
