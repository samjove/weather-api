import requests
from flask import Flask, request
from decouple import config

app = Flask(__name__)

WEATHER_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
API_KEY = config('API_KEY')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    get_url = f'{WEATHER_URL}{city}?key={API_KEY}'
    return requests.get(get_url).content
    
if __name__ == '__main__':
    app.run(port=5000)