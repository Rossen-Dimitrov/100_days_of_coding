import requests

API_KEY = "10a8c8d9762dfe36266142aee6d47ca1"
OW_API = "https://api.openweathermap.org/data/2.5/weather"
OW_ONE_CALL_API = "https://api.openweathermap.org/data/3.0/onecall"

one_caa_params = {
    "lat": 42.6975,
    "lon": 23.3242,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
parameters = {
    "q": "Sofia,BG",
    "appid": API_KEY
}

response = requests.get(OW_ONE_CALL_API, params=one_caa_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")