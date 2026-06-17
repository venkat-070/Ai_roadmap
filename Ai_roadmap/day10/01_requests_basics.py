import requests as r

response = r.get("https://wttr.in/London?format=j1")

print(response.status_code)
d = response.json()
print(type(d))

for i in d.keys():
    print(i)

current = d["current_condition"][0]
print("Temperature: "+current['temp_C']+"°C")
print("Feels Like: "+current['FeelsLikeC']+"°C")
print("Humidity: "+current['humidity']+"%")
print("Description: "+current['weatherDesc'][0]['value'])
print("Wind Speed: "+current['windspeedKmph']+" Km/h")
