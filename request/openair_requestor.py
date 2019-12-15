import requests
import json

class OpenAirRequestor(object):
    def _init_(self):
        self.openair_url = 'https://api.openaq.org/v1/latest?city={}'

    def get_quality(city):
        URL = self.openair_url.format(city)
        r = requests.get(URL)
        return json.loads(r.text)['results']
