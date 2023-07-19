from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city='Dhanbad'):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__=='__main__':

    print('\n**** Get Current Weather Condition ****\n')

    city_name = input('Enter your city name\n')

    if not bool(city_name.strip()):
        city_name = 'Dhanbad'

    weather_data = get_current_weather(city_name)
    print('\n')
    pprint(weather_data)