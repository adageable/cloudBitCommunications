# to find the address of your hue bridge: https://www.meethue.com/api/nupnp

import requests
import json

class Hue:
    def __init__(self, device_id):

        r = requests.get("https://www.meethue.com/api/nupnp")
        jsonresult = json.loads(r.text)
        self.ipaddress = jsonresult[0]['internalipaddress']

    def stream(self):
        print "nothing"