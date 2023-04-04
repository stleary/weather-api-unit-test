import requests



def manipulate_weather_data():
    api_key = "go get your own api key and put it here"
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