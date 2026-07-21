import requests

city = input("Enter city name:")
url = f"https://wttr.in/(city)?format=j1"
data = requests.get(url).json()

temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
humidity = data["current_condition"][0]["humidity"]

print("\n City:", city)
print("\n Temperature:", temp, "°C")
print("\n Weather:", weather)
print("\n Humidity:", humidity, "%")
