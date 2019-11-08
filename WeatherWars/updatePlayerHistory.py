#!/usr/bin/env python
# coding: utf-8

# In[2]
import requests
import json
import pyodbc
from datetime import date
from datetime import datetime
from time import sleep


# In[3]:


def updatePlayerHistory(cId, duration, weatherType, scoringType, conn, cursor):
    if duration == 'Daily':
        price = 10
    elif duration == 'Weekly': 
        price = 50
    else:
        price = 300
    if(weatherType == 'Heat' and scoringType == 'Extremes'):
        cursor.execute("select count(userName) from finishedContestScoresExtremes where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, HeatScore from finishedContestScoresExtremes where contest# = ? "
                       "order by HeatScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    elif(weatherType == 'Heat' and scoringType == 'Predictions'):
        cursor.execute("select count(userName) from finishedContestScoresPredictions where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, HeatScore from finishedContestScoresPredictions where contest# = ? "
                       "order by HeatScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    elif(weatherType == 'Cold' and scoringType == 'Extremes'):
        cursor.execute("select count(userName) from finishedContestScoresExtremes where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, ColdScore from finishedContestScoresExtremes where contest# = ? "
                       "order by ColdScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    elif(weatherType == 'Cold' and scoringType == 'Predictions'):
        cursor.execute("select count(userName) from finishedContestScoresPredictions where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, ColdScore from finishedContestScoresPredictions where contest# = ? "
                       "order by ColdScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    elif(weatherType == 'Rain' and scoringType == 'Extremes'):
        cursor.execute("select count(userName) from finishedContestScoresExtremes where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, RainScore from finishedContestScoresExtremes where contest# = ? "
                       "order by RainScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    elif(weatherType == 'Rain' and scoringType == 'Predictions'):
        cursor.execute("select count(userName) from finishedContestScoresPredictions where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, RainScore from finishedContestScoresPredictions where contest# = ? "
                       "order by RainScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    elif(weatherType == 'Wind' and scoringType == 'Extremes'):
        cursor.execute("select count(userName) from finishedContestScoresExtremes where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, RainScore from finishedContestScoresExtremes where contest# = ? "
                       "order by WindScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    else:
        cursor.execute("select count(userName) from finishedContestScoresPredictions where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        cursor.execute("select userName, RainScore from finishedContestScoresPredictions where contest# = ? "
                       "order by WindScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize,streaks[1]+1,streaks[1]+1, row[0]))
                else:
                    cursor.execute("update history set earnings = earnings+?, currentStreak = currentStreak+1, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize, row[0]))
            elif count == 1:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames = totalGames+1, "
                               "where userName = ?",(secondPrize, row[0]))
            elif count == 2:
                cursor.execute("update history set earnings = earnings+?, currentStreak = 0, totalGames=totalGames+1, " 
                               "where userName = ?",(thirdPrize,row[0]))
            else:
                cursor.execute("update history set earnings = earnings - ?, currentStreak = 0, "
                               "totalGames = totalGames+1 where userName = ?", (price, row[0]))
            count = count + 1
    conn.commit()      


