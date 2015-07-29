#ex40a.py
from ex40 import *

happy_bday = Song(['Happy Birthday to you','You live in a shoe','You smell like a monkey','and you look like one too.'])

rain_rain = Song(['rain rain','go away','come again', 'another day'])

polly = Bird("squawk squawk")
harry = Bird("Tweet Tweet")

happy_bday.sing_me_a_song()
print("\nPolly says: ", polly.talk())
print("\nHarry says: ", harry.talk())
rain_rain.sing_me_a_song()