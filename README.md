# Weather API 
This is a simple Flask web application that serves weather data for a given city. The application caches the weather data using Redis to improve performance and reduce the number of API calls to the third-party weather service.

## Features

- Fetches weather data from a third-party API based on the `city` query parameter.
- Caches the weather data in Redis to improve performance and reduce redundant API calls.
- Rate limits the api to a fixed window. 
- Handles errors such as missing query parameters or third-party API failures.

## Installation

### Clone the repository:

`git clone https://github.com/samjove/weather-api.git`

`cd weather-api`

### Set up a virtual environment (optional):

`python3 -m venv venv`

`source venv/bin/activate` 

On Windows, use `venv\Scripts\activate`


### Install the required Python packages:

`pip install -r requirements.txt`

### Install Redis:

Installation page with links for OS-specific instrutctions, [here](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/).

### Set up environment variables:

You can create a `.env` file to store the weather api key, which you can obtain by signing up for an account [here](https://www.visualcrossing.com/).

Redis related configuration variables are stored on the script itself for convenience, since they are defaults.

## Running the Application

### Start the Flask application:

`flask --app api run`

By default, the app will be available at `http://127.0.0.1:5000`.

### Make requests to the API:

You can make a GET request to the `/weather` endpoint with the `city` query parameter to fetch weather data.


`curl "http://127.0.0.1:5000/weather?city=Boston"`

The first request will fetch data from the third-party API and cache it. Subsequent requests for the same city within the cache timeout period will return the cached response.

### Use the Redis CLI to monitor keys and check cached values.

In redis-cli enter  `KEYS *`

See project requirements [here](https://roadmap.sh/projects/weather-api-wrapper-service).