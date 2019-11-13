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
    cursor.execute("select * from cities")
    values = cursor.fetchone()
    if values == None:
        cityCommands = ["insert into cities (cName, geoId, cState) values ('Boston','Coastal', 'MA')",
                    "insert into cities (cName, geoId, cState) values ('Minneapolis', 'Land-Locked', 'MN')",
                   "insert into cities (cName, geoId, cState) values ('Detroit', 'Land-Locked', 'MI')",
                   "insert into cities (cName, geoId, cState) values ('Chicago', 'Land-Locked', 'IL')",
                   "insert into cities (cName, geoId, cState) values ('Seattle','Coastal', 'WA')",
                   "insert into cities (cName, geoId, cState) values ('Phoenix', 'Desert', 'AZ')",
                   "insert into cities (cName, geoId, cState) values ('Miami','Coastal','FL')",
                   "insert into cities (cName, geoId, cState) values ('Portland','Coastal','OR')",
                   "insert into cities (cName, geoId, cState) values ('Atlanta', 'Land-Locked', 'GA')",
                   "insert into cities (cName, geoId, cState) values ('Honolulu', 'Coastal', 'HI')",
                   "insert into cities (cName, geoId, cState) values ('Juneau', 'Coastal', 'AL')",
                   "insert into cities (cName, geoId, cState) values ('Houston', 'Land-Locked', 'TX')",
                   "insert into cities (cName, geoId, cState) values ('Helena', 'Land-Locked', 'MT')",
                   "insert into cities (cName, geoId, cState) values ('Pittsburgh', 'Land-Locked', 'PA')",
                   "insert into cities (cName, geoId, cState) values ('Denver', 'Land-Locked', 'CO')",
                   "insert into cities (cName, geoId, cState) values ('Boulder', 'Land-Locked', 'CO')",
                   "insert into cities (cName, geoId, cState) values ('Sacramento', 'Land-Locked', 'CA')",
                   "insert into cities (cName, geoId, cState) values ('San Jose', 'Coastal', 'CA')",
                   "insert into cities (cName, geoId, cState) values ('San Francisco', 'Coastal', 'CA')",
                   "insert into cities (cName, geoId, cState) values ('New York', 'Coastal', 'NY')",
                   "insert into cities (cName, geoId, cState) values ('Los Angeles', 'Coastal', 'CA')",
                   "insert into cities (cName, geoId, cState) values ('Las Vegas', 'Desert', 'NV')"]

        for line in cityCommands:
            cursor.execute(line)
    conn.commit()


# In[ ]:




