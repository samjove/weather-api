import requests
from flask import Flask, request
from decouple import config
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from requests.exceptions import RequestException


# Configures and initializes Flask app with Cache for Redis.
cache_config = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_HOST": "localhost",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
}
app = Flask(__name__)
cache = Cache(config=cache_config)
cache.init_app(app)


# Sets up Flask Limiter to rate limit api.
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379",
    strategy="fixed-window",
)

WEATHER_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
API_KEY = config("API_KEY")

# Defines cache key as the 'city' query parameter.
def make_city_key():
    return request.args.get("city")


# Decorators set the route and HTTP method, the rate limit, and the cache settings.
@app.route("/weather", methods=["GET"])
@limiter.limit("10/hour")
@cache.cached(timeout=43200, make_cache_key=make_city_key)
def get_weather():
    city = request.args.get("city")

    # If city parameter is present, makes api call, raising an error on an undesired response.
    if not city:
        return {'Missing "city" query parameter'}, 400
    try:
        get_url = f"{WEATHER_URL}{city}?key={API_KEY}"
        response = requests.get(get_url, timeout=5)
        response.raise_for_status()
        return response.content
    except RequestException as e:
        return {"Failed to retrive weather data", str(e)}, 502


if __name__ == "__main__":
    app.run(port=5000)
