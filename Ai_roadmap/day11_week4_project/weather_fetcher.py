import requests as r
def get_weather(city):
    try:
        url = "https://wttr.in/" + city + "?format=j1"
        response = r.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("City not found or api error")
            return None
    except Exception as e:
        print("Connection error "+str(e))
        return None
def display_weather(data,city):
    if not data:
        print("no data found!!")
        return None
    else:
        current = data["current_condition"][0]
    print("======================================\nWeather in "+city+"\n======================================")
    print("Temperature: "+current['temp_C']+"°C")
    print("Feels Like: "+current['FeelsLikeC']+"°C")
    print("Humidity: "+current['humidity']+"%")
    print("Description: "+current['weatherDesc'][0]['value'])
    print("Wind Speed: "+current['windspeedKmph']+" Km/h")
    print("======================================")

while True:
    print("1. check weather\n2. Exit")
    i = input("Select an option: ")
    if i == "1":
        city = input("Enter city name: ")
        data = get_weather(city)
        display_weather(data,city)
    elif i == "2":
        break
    else:
        print("Invalid input!")