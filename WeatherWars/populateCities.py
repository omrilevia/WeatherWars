#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import json
import pyodbc
from datetime import date
from datetime import datetime


# In[2]:


#conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      #'Server=LAPTOP-RC2ANL8F\SQLEXPRESS;'
                      #'Database=WeatherWars;'
                      #'Trusted_Connection=yes;')
#cursor = conn.cursor()


# In[3]:


def populateCities(conn, cursor):
    cityCommands = ["insert into WeatherWars.dbo.cities values ('Boston','Coastal', 'MA')",
                    "insert into WeatherWars.dbo.cities values ('Minneapolis', 'Land-Locked', 'MN')",
                   "insert into WeatherWars.dbo.cities values ('Detroit', 'Land-Locked', 'MI')",
                   "insert into WeatherWars.dbo.cities values ('Chicago', 'Land-Locked', 'IL')",
                   "insert into WeatherWars.dbo.cities values ('Seattle','Coastal', 'WA')",
                   "insert into WeatherWars.dbo.cities values ('Phoenix', 'Desert', 'AZ')",
                   "insert into WeatherWars.dbo.cities values ('Miami','Coastal','FL')",
                   "insert into WeatherWars.dbo.cities values ('Portland','Coastal','OR')",
                   "insert into WeatherWars.dbo.cities values ('Atlanta', 'Land-Locked', 'GA')",
                   "insert into WeatherWars.dbo.cities values ('Honolulu', 'Coastal', 'HI')",
                   "insert into WeatherWars.dbo.cities values ('Juneau', 'Coastal', 'AL')",
                   "insert into WeatherWars.dbo.cities values ('Houston', 'Land-Locked', 'TX')",
                   "insert into WeatherWars.dbo.cities values ('Helena', 'Land-Locked', 'MT')",
                   "insert into WeatherWars.dbo.cities values ('Pittsburgh', 'Land-Locked', 'PA')",
                   "insert into WeatherWars.dbo.cities values ('Denver', 'Land-Locked', 'CO')",
                   "insert into WeatherWars.dbo.cities values ('Boulder', 'Land-Locked', 'CO')",
                   "insert into WeatherWars.dbo.cities values ('Sacramento', 'Land-Locked', 'CA')"
                   "insert into WeatherWars.dbo.cities values ('San Jose', 'Coastal', 'CA')",
                   "insert into WeatherWars.dbo.cities values ('San Francisco', 'Coastal', 'CA')",
                   "insert into WeatherWars.dbo.cities values ('New York', 'Coastal', 'NY')",
                   "insert into WeatherWars.dbo.cities values ('Los Angeles', 'Coastal', 'CA')",
                   "insert into WeatherWars.dbo.cities values ('Las Vegas', 'Desert', 'NV')"]

    for line in cityCommands:
        cursor.execute(line)
    conn.commit()


# In[ ]:




