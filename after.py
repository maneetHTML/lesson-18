import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'City': data['name'],
            'Temperature': f"{data['main']['temp']} °C",
            'Weather': data['weather'][0]['description'].title(),
            'Humidity': f"{data['main']['humidity']}%",
            'Wind Speed': f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return f"Error: {response.status_code} - {response.json().get('message', 'Unable to fetch data')}"

# Example usage:
if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "d22b8eb118b26b6506a74feed80f92ac"  # Replace with your actual OpenWeatherMap API key
    
    weather_info = get_weather(city, api_key)
    print("\nWeather Information:")
    if isinstance(weather_info, dict):
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    else:
        print(weather_info)
