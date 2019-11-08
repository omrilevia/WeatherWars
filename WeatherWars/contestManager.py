#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
import pandas as pd
import json
import pyodbc
from updatePlayerHistory import updatePlayerHistory
from datetime import date
from datetime import datetime
from time import sleep


# In[17]:


#conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      #'Server=LAPTOP-RC2ANL8F\SQLEXPRESS;'
                      #'Database=WeatherWars;'
                      #'Trusted_Connection=yes;')
#cursor = conn.cursor()


# In[ ]:


def dailyContest(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Daily','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Heat','Daily','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Cold','Daily','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Cold','Daily','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Wind','Daily','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Wind','Daily','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Rain','Daily','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Rain','Daily','Extremes','classic',?,'Pending')",(now))
    
    conn.commit()

def dailyContestHeatExtremes(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Daily','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def dailyContestHeatPredictions(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Daily','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def dailyContestColdExtremes(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Cold','Daily','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def dailyContestColdPredictions(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Cold','Daily','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def dailyContestWindExtremes(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Wind','Daily','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def dailyContestWindPredictions(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Wind','Daily','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def dailyContestRainExtremes(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Rain','Daily','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def dailyContestRainPredictions(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Rain','Daily','Predictions','classic',?,'Pending')",(now))
    conn.commit()


# In[21]:


def weeklyContest(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Weekly','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Heat','Weekly','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Cold','Weekly','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Cold','Weekly','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Wind','Weekly','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Wind','Weekly','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Rain','Weekly','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Rain','Weekly','Extremes','classic',?,'Pending')",(now))
    
    conn.commit()

def weeklyContestHeatExtremes(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Weekly','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def weeklyContestHeatPredictions(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Weekly','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def weeklyContestColdExtremes(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Cold','Weekly','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def weeklyContestColdPredictions(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Cold','Weekly','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def weeklyContestWindExtremes(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Wind','Weekly','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def weeklyContestWindPredictions(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Wind','Weekly','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def weeklyContestRainExtremes(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Rain','Weekly','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def weeklyContestRainPredictions(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Rain','Weekly','Predictions','classic',?,'Pending')",(now))
    conn.commit()


# In[22]:


def seasonalContest(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Seasonal','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Heat','Seasonal','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Cold','Seasonal','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Cold','Seasonal','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Wind','Seasonal','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Wind','Seasonal','Predictions','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Rain','Seasonal','Extremes','classic',?,'Pending')",(now))
    cursor.execute("insert into contest values ('Rain','Seasonal','Predictions ','classic',?,'Pending')",(now))
    
    conn.commit()

def seasonalContestHeatExtremes(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Seasonal','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def seasonalContestHeatPredictions(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Heat','Seasonal','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def seasonalContestColdExtremes(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Cold','Seasonal','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def seasonalContestColdPredictions(cursor,conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Cold','Seasonal','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def seasonalContestWindExtremes(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Wind','Seasonal','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def seasonalContestWindPredictions(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Wind','Seasonal','Predictions','classic',?,'Pending')",(now))
    conn.commit()

def seasonalContestRainExtremes(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Rain','Seasonal','Extremes','classic',?,'Pending')",(now))
    conn.commit()

def seasonalContestRainPredictions(cursor, conn):
    now = datetime.now()
    cursor.execute("insert into contest values ('Rain','Seasonal','Predictions','classic',?,'Pending')",(now))
    conn.commit()


# In[4]:


def updateContestsAndCreateNew(conn, cursor):
    now = datetime.now()
    cursor.execute("select * from contest")
    val = cursor.fetchone()
    if val == None:
        dailyContest(cursor,conn)
        weeklyContest(cursor,conn)
        seasonalContest(cursor,conn)
    cursor.execute("select cId, Duration, timeCreated from contest where status = 'Pending'")
    values = cursor.fetchall()
    for row in values:
        delta = now - row[2]
        if(row[1] == 'Daily' and delta.days > 0):
            cursor.execute("update contest set status = 'Running' where cId = ?", (row[0]))
        if(row[1] == 'Weekly' and delta.days > 2):
            cursor.execute("update contest set status = 'Running' where cId = ?", (row[0]))
        if(row[1] == 'Seasonal' and delta.days > 6):
            cursor.execute("update contest set status = 'Running' where cId = ?", (row[0]))
    conn.commit()
    
    now = datetime.now()
    cursor.execute("select cId, Duration, timeCreated, weatherType, scoringType from contest where status = 'Running'")
    values = cursor.fetchall()
    for row in values:
        delta = now - row[2]
        if(row[1] == 'Daily' and delta.days > 1):
            cursor.execute("update contest set status = 'Finished' where cId = ?", (row[0]))
            # call function to update user history here i.e. determine winners
            updatePlayerHistory(row[0], row[1], row[3], row[4], conn, cursor)
            # create new daily here
            if(row[3] == 'Heat' and row[4] == 'Extremes'):
                dailyContestHeatExtremes(cursor,conn)
            if(row[3] == 'Heat' and row[4] == 'Predictions'):
                dailyContestHeatPredictions(cursor,conn)
            if(row[3] == 'Cold' and row[4] == 'Extremes'):
                dailyContestColdExtremes(cursor,conn)
            if(row[3] == 'Cold' and row[4] == 'Predictions'):
                dailyContestColdPredictions(cursor,conn)
            if(row[3] == 'Wind' and row[4] == 'Extremes'):
                dailyContestWindExtremes(cursor,conn)
            if(row[3] == 'Wind' and row[4] == 'Predictions'):
                dailyContestWindPredictions(cursor,conn)
            if(row[3] == 'Rain' and row[4] == 'Extremes'):
                dailyContestRainExtremes(cursor,conn)
            if(row[3] == 'Rain' and row[4] == 'Predictions'):
                dailyContestRainPredictions(cursor,conn)
        if(row[1] == 'Weekly' and delta.days > 9):
            cursor.execute("update contest set status = 'Finished' where cId = ?", (row[0]))
            # call function to update user history here, i.e. determine winners
            updatePlayerHistory(row[0], row[1], row[3], row[4], conn, cursor)
            # create new weekly here (?)
            if(row[3] == 'Heat' and row[4] == 'Extremes'):
                weeklyContestHeatExtremes(cursor,conn)
            if(row[3] == 'Heat' and row[4] == 'Predictions'):
                weeklyContestHeatPredictions(cursor,conn)
            if(row[3] == 'Cold' and row[4] == 'Extremes'):
                weeklyContestColdExtremes(cursor,conn)
            if(row[3] == 'Cold' and row[4] == 'Predictions'):
                weeklyContestColdPredictions(cursor,conn)
            if(row[3] == 'Wind' and row[4] == 'Extremes'):
                weeklyContestWindExtremes(cursor,conn)
            if(row[3] == 'Wind' and row[4] == 'Predictions'):
                weeklyContestWindPredictions(cursor,conn)
            if(row[3] == 'Rain' and row[4] == 'Extremes'):
                weeklyContestRainExtremes(cursor,conn)
            if(row[3] == 'Rain' and row[4] == 'Predictions'):
                weeklyContestRainPredictions(cursor,conn)
        if(row[1] == 'Seasonal' and delta.days > 96):
            cursor.execute("update contest set status = 'Finished' where cId = ?", (row[0]))
            # call function to update user history here i.e. determine winners
            updatePlayerHistory(row[0], row[1], row[3], row[4], conn, cursor)
            # create new seasonal here (?)
            if(row[3] == 'Heat' and row[4] == 'Extremes'):
                seasonalContestHeatExtremes(cursor,conn)
            if(row[3] == 'Heat' and row[4] == 'Predictions'):
                seasonalContestHeatPredictions(cursor,conn)
            if(row[3] == 'Cold' and row[4] == 'Extremes'):
                seasonalContestColdExtremes(cursor,conn)
            if(row[3] == 'Cold' and row[4] == 'Predictions'):
                seasonalContestColdPredictions(cursor,conn)
            if(row[3] == 'Wind' and row[4] == 'Extremes'):
                seasonalContestWindExtremes(cursor,conn)
            if(row[3] == 'Wind' and row[4] == 'Predictions'):
                seasonalContestWindPredictions(cursor,conn)
            if(row[3] == 'Rain' and row[4] == 'Extremes'):
                seasonalContestRainExtremes(cursor,conn)
            if(row[3] == 'Rain' and row[4] == 'Predictions'):
                seasonalContestRainPredictions(cursor,conn)
    conn.commit()        


# In[ ]:




