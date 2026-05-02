import requests

def get_weather(city):
    api_key = "c321baef6f214b2c09ee011ba4ff7640"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data["cod"] != 200:
            print("City not found! Please try again.")
            return
        
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition.capitalize()}")
        print(f"Humidity: {humidity}%\n")
        
    except Exception as e:
        print("Error fetching weather:", e)

def main():
    print("Welcome to PyWeather!")
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
