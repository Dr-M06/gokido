def get_weather(city):
  api_key = "439835ee04a1956013dfa2180fb18073"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city
  response = requests.get(complete_url)
  if response.status_code == 200:
    return response.json()
  else:
    return "Error: Could not retrieve weather data"

def display_weather(weather):
    temperature = weather['main']['temp']
    celsius = temperature - 273.15
    celsius = round(celsius)
    celsius = int(celsius)
    print(f"Temperature: {celsius}°C")
    print(f"Sky: {weather['weather'][0]['main']}")
    print(f"Description: {weather['weather'][0]['description']}")

city = input("Enter your city: ")
weather = get_weather(city)
display_weather(weather)

#created by M06
#instagram @dr_m06
