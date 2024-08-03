import tests_datetime as dt
from tests_datetime import datetime, timedelta #also so i can access days ahead
import requests

api_key = '65ec67aa1a3f45a2b8d746ee7b0ab4e3'

first_holiday_city = ""  # declare holiday_city globally - globally so i can use this variable on line139 when new file is created
second_holiday_city = ""  #declare second_holiday_city globally for same reason as above


def kelvin_to_celsius(kelvin): #function to convert to celsius
    celsius = kelvin - 273.15
    return celsius

def display_weather_icons(weather_description): #function to display wweather icon based on weather description
    weather_icons = {
        'sunny': '☀️☀️',
        'clear': '🌤🌤',
        'clouds': '☁️☁️',
        'rain': '🌧🌧',
        'thunderstorm': '🌩🌩',
        'snow': '❅☃️',
        'mist': '🌫🌫',
    }
    for key, value in weather_icons.items(): #starts a loop that iterates over the icons in the weather_icons dictionary. key = sun/rain/clear etc
        if key in weather_description.lower(): #.lower to convert all the characters lowercase for consistency
            return value
    return ''

def suggested_activity(weather_description): #function that suggest activities ai&user can do based on the weather description
    if 'rain' in weather_description.lower():
        return "Lets go on a walk in the rain - you better not straighten your hair!💆🏼‍"
    elif 'hot' in weather_description.lower():
        return "About time we get some sun!! Lets get a tan!🌞"
    elif 'clear' in weather_description.lower():
        return "We should defo have a brunch outside!🥗🍴"
    elif 'clouds' in weather_description.lower():
        return "Maybe we can stay in and watch a movie on this day🍿"
    else:
        return "Let's have the bestest day ever!🤪🤪"

def main():
    global first_holiday_city #as mentioned on line7&8, already declared
    global second_holiday_city

    user_name = input('Hey!🦾🤪 I am your weather AI bestie! What\'s your name?: ')
    print(f"Hi {user_name} 💐🥰!")

    city = input('Which city are you interested in looking at first?: ')

    baseURL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}' #this is fetching the weather data for the selected city the user writes in
    response = requests.get(baseURL)

    if response.status_code == 404: #404=not found. if the code doesnt work, print:
        print("HMM that's not a city.. maybe check the spelling??")
    else:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like_kelvin = data['main']['feels_like']
        temp_celsius = round(kelvin_to_celsius(temperature))
        feels_like_celsius = round(kelvin_to_celsius(feels_like_kelvin))
        icon = display_weather_icons(weather_description)

        print(f"Nice! So the general weather in {city} is {weather_description} {icon}.")
        print(
            f"The current temperature there is: {temp_celsius:.0f}°C , and feels like: {feels_like_celsius:.0f}°C (could be worse!!)")

        keep_planning = input(
            "We're about to plan the most spontaneous trip. You're still interested, right??🫡 (yes/no): ").lower() == 'yes'
        if not keep_planning:
            print("Okay, you're missing out! Cya!!")
            return  # Stop execution if the user doesn't want to proceed with planning. else, keep going

        first_holiday_city = input('SO! As your BFFL, if we were to go on holiday in 3 days time, which city should we go to? (somewhere hot please!!): ')
        target_date = datetime.now() + timedelta(days=3) #to see the weather in 3 days time

        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
        forecast_response = requests.get(forecast_url)

        if forecast_response.status_code == 200: #if the forecast data is avaliable, get the data from the json file
            forecast_data = forecast_response.json()

            for forecast in forecast_data['list']: #searching for the forecast data of the targetted date put through
                forecast_date = datetime.fromtimestamp(forecast['dt'])

                if forecast_date.date() == target_date.date():
                    temperature = round(forecast['main']['temp'] - 273.15)
                    description = forecast['weather'][0]['description']

                    print(
                        f"Nice choice bestie!!! On {target_date.date()}, the temperature in {first_holiday_city} will be {temperature}°C and the weather will be {description} - not bad at all!")
                    break
            else:
                print("Forecast data not available for the given date.")
        else:
            print("Error fetching forecast data.")

        baseURL = f'http://api.openweathermap.org/data/2.5/weather?q={first_holiday_city}&appid={api_key}'
        response = requests.get(baseURL)

        if response.status_code == 404: #checks to see if the city the user put through exists
            print("HMM i dont recognise that city.. maybe check the spelling??")
        else:
            data = response.json()
            weather_description = data['weather'][0]['description']

            print(suggested_activity(weather_description)) #displays activity suggestion

        second_holiday_city = input(
            "EXCITING!!! OK I think we should only stay there for 24 hours and go somewhere else the next day!! I was thinking Madrid, but where would you like to go??:")


        baseURL = f'http://api.openweathermap.org/data/2.5/weather?q={second_holiday_city}&appid={api_key}' #fetching data for the second city
        response = requests.get(baseURL)

        if response.status_code == 404:
            print("HMM I haven't seen that spelling before...")
        else:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            feels_like_kelvin = data['main']['feels_like']
            round(kelvin_to_celsius(temperature))
            round(kelvin_to_celsius(feels_like_kelvin))
            display_weather_icons(weather_description)
            sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone']) + timedelta(days=4) #gets the time of the sunset/sunrise on the fourth day from the current date
            sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone']) + timedelta(days=4) # ^^

            print(
                f"This will be soo cute! If we get to {second_holiday_city} before {sunrise_time.strftime('%H:%M')}am, we'll get to see the sun rise 🌇☄️")
            print(
                f"But if we miss that, we can still watch the sun set at {sunset_time.strftime('%H:%M')}pm. How cute! 🌗🌙 ")
            print("I'm so excited for this trip! 💓")

if __name__ == "__main__":
    main()
    with open('besties_holiday_plan.txt', 'w') as file:
        file.write(f"We are going to have the most crazy holiday in {first_holiday_city} and {second_holiday_city} 😁🤪🦾!!!!\n")
        #the string with varibale that will be displayed in new file