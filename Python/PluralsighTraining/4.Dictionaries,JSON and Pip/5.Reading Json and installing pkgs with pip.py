#Program that will request data from online and present it
#Want it to mkae a request to a webserver and then present this information on the page
#need to install pip to download packages and use request to request data information on the web
import requests

response= requests.get("http://api.open-notify.org/astros.json")
#response is being set to a request for getting the json data from the server
json = response.json()
#setting a variable called json to equal the data that is received from the server
print(json)
print("The people currently in space are:")
for person in json["people"]:
    print(person["name"])
