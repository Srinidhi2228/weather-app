import requests

from config import API_KEY


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")

url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"

print("\n🔗 API URL:", url)   # Debugging line
response = requests.get(url).json()

print("\n📩 Raw Response:", response)   # Debugging line

if response["cod"] == 200:
    print("\n--- Weather Report ---")
    print(f"City: {response['name']}")
    print(f"🌡️ Temperature: {response['main']['temp']}°C")
    print(f"💧 Humidity: {response['main']['humidity']}%")
    print(f"🌬️ Wind Speed: {response['wind']['speed']} m/s")
    print(f"☁️ Condition: {response['weather'][0]['description']}")
else:
    print("❌ Error:", response["message"])
