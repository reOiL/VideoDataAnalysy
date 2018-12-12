import json
import datetime

data = {'1': {'time': '2018-02-11 15:00:00', 'ERROR': 3}}


class emulator:
    def __init__(self):
        self.data = json.load(open('event_emu.json', 'r'))

    def pop_event(self):
        pass
        #for i in self.data:

            #if -self.data[i]
             #   pass
