from bitClass import Bit as cloudbit
from secrets import *
# load bitAccessToken adn bitDeviceId from secrets.py file

bit = cloudbit(secretBitAccessToken, secretBitDeviceId)

#for pct in bit.raw_stream():
#    print pct.type

for x in range(0, 50):
    print x
    bit.output(99, 50)
    bit.output(0, 50)

# print bit.input()
# this pulls a single measurement from the item

