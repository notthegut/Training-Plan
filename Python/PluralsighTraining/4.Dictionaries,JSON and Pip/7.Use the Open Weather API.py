import requests
city = "Orlando"
url = "http://api.weatherapi.com/v1/current.json?key=7677e48133b9402e908172031241911&q="+city+"&aqi=no"
#We have made city a variable and changed the position for cities in the url key to be that variable
#This allows us to change the city and get the information for that city as we need
response = requests.get(url)
weather_json = response.json()

print(weather_json)

temp=weather_json.get("current").get("temp_c")
print(temp)

description = weather_json.get("current").get("condition").get("text")
print(description)

