import requests
import json


class OpenAirRequestor(object):
    def __init__(self):
        self.openair_url = 'https://api.openaq.org/v1/latest?city={}'

    def get_quality(self, city):
        URL = self.openair_url.format(city)
        r = requests.get(URL)
        return json.loads(r.text)['results']
