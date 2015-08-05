# to find the address of your hue bridge: https://www.meethue.com/api/nupnp

import requests
import json


class Hue:
    def __init__(self, device_id):

        r = requests.get("https://www.meethue.com/api/nupnp")
        jsonresult = json.loads(r.text)
        self.ipaddress = jsonresult[0]['internalipaddress']
        self.device_id = device_id

    # TODO Update this to search for light from enumeration by name (e.g. Zoes Lamp)
    def setstate(self, d, lightnum):
        print 'http://%s/api/%s/lights/%s/state' % (self.ipaddress, self.device_id, 1)
        r = requests.put('http://%s/api/%s/lights/%s/state' % (self.ipaddress, self.device_id, lightnum), data=json.dumps(d))
        # print r.json()


