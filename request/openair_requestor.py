import requests
import json


class OpenAirRequestor(object):
    
    '''
    OpenAirRequestor class does the following:
    - send a request to the OpenAQ server for the given city
    '''
    
    def __init__(self):
        self.openair_url = 'https://api.openaq.org/v1/latest?city={}'

    def get_quality(self, city):
        URL = self.openair_url.format(city)
        r = requests.get(URL)
        return json.loads(r.text)['results']
