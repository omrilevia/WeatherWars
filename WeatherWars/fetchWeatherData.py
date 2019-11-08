#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import json
import pyodbc
from datetime import date
from datetime import datetime
from time import sleep

def fetchWeatherData(conn, cursor):
    urls = ['http://api.openweathermap.org/data/2.5/weather?q=San%20Francisco,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=San%20Jose,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=New%20York,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Boston,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Los%20Angeles,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Las%20Vegas,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Minneapolis,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Detroit,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Chicago,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Seattle,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Phoenix,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Miami,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Portland,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Atlanta,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Honolulu,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Juneau,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Houston,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Helena,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Pittsburgh,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Denver,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374',
    'http://api.openweathermap.org/data/2.5/weather?q=Boulder,US&units=imperial&APPID=de2e3055b593558ad302dda095e9f374']

    cityWeather = []
    for row in urls:
        response = requests.get(row)
        responseDict = response.json()
        responseJSON = json.dumps(responseDict)
        data = json.loads(responseJSON)
        cityWeather.append(data)

    for row in cityWeather:
        temp = row['main']['temp']
        try:
            row['rain']['1h']
            rain = row['rain']['1h']
        except:
            rain = 0
        wind = row['wind']['speed']
        name = row['name']
        today = date.today()
        now = datetime.now()
        cursor.execute("select tHigh, tLow, rainLevel, windSpeed from weather where cName = ? and currentDate = ?",(name, today))
        values = cursor.fetchone()
        if values != None:
            high = values[0]
            low = values[1]
            rainL = values[2]
            windS = values[3]
        
            if temp > high:
                cursor.execute("update weather set tHigh = ?, lastUpdated = ? where cName = ? and currentDate = ?", (temp, now, name, today))
            if temp < low:
                cursor.execute("update weather set tLow = ?, lastUpdated = ? where cName = ? and currentDate = ?", (temp, now, name, today))
            if rain > rainL:
                cursor.execute("update weather set rainLevel = ?, lastUpdated = ? where cName = ? and currentDate = ?", (rain, now, name, today))
            if wind > windS:
                cursor.execute("update weather set windSpeed = ?, lastUpdated = ? where cName = ? and currentDate = ?", (wind, now, name, today))
        else:
            cursor.execute("insert into weather values(?,?,?,?,?,?,?)",(name, now, today, temp, temp, rain, wind))
    conn.commit()


# In[ ]:




