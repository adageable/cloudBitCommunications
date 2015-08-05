# Test application for turning on a light

from hueFunctions import Hue
from secrets import *


hue = Hue(secretHueDeviceId)
print hue.ipaddress


d1 = {
    'on': True,
    'bri': 255,  # 0..255
    'hue': 0,  # 0 and 65535. Both 0 and 65535 are red, 25500 is green and 46920 is blue.
    'sat': 0,   # 0..255
}

d2 = {
    'on': False,
}

hue.setstate(d2, 3)



