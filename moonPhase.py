import requests as req
import json
from datetime import date

class moonData():
    '''Class moondata, serves data regarding the moons phases'''
    def __init__(self, date, key):
        self.key = key
        self.date = date

    def api(self):
        self.makeString = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Brisbane,QLD/{self.date}?unitGroup=us&key={self.key}&include=days&elements=datetime,moonphase,sunrise,sunset'

    def gather(self):
        res = (req.get(self.makeString)).json()
        days = res['days'][0]
        self.moonphase = days['moonphase']

    def moonOut(self):
        if self.moonphase==0:
            print(f"Tonight is a new moon; {self.moonphase}")
        elif self.moonphase<0.25:
            print(f"Tonight is a waxing crescent moon; {self.moonphase}")
        elif self.moonphase==0.25:
            print(f"Tonight is the first quarter; {self.moonphase}")
        elif self.moonphase<0.5:
            print(f"Tonight is waxing gibbous; {self.moonphase}")
        elif self.moonphase==0.5:
            print(f"Tonight is a full moon; {self.moonphase}")
        elif self.moonphase>0.75:
            print(f"Tonight is a waning gibbous; {self.moonphase}")
        elif self.moonphase==0.75:
            print(f"Tonight is the last quarter; {self.moonphase}")
        elif self.moonphase<1:
            print(f"Tonight is a waning crescent; {self.moonphase}")

key = ''
date = date.today()

if __name__ == '__main__':
    #print(help(moonData(date, key)))
    moon = moonData(date, key)
    moon.api()
    moon.gather()
    moon.moonOut()
