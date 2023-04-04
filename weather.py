import requests



def get_weather_data():
    api_key = "your own api key here"
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York".format(api_key)

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["current"]["temperature"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_speed"]
        return temperature, humidity, wind_speed
    else:
        raise Exception("Failed to retrieve weather data")