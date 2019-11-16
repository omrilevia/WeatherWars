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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesDaily where contest# = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesWeekly where contest# = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresExtremesSeasonal where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, HeatScore from finishedContestScoresExtremesDaily where contest# = ? "
                       "order by HeatScore desc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, HeatScore from finishedContestScoresExtremesWeekly where contest# = ? "
                       "order by HeatScore desc",(cId))
        else:
            cursor.execute("select userName, HeatScore from finishedContestScoresExtremesSeasonal where contest# = ? "
                       "order by HeatScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchone()
                if (streaks[0] == streaks[1] and streaks[0] > 2):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1,streaks[1]+1,streaks[1]+1, row[0]))
                elif(streaks[0] == streaks[1]):
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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsDaily where contest# = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsWeekly where contest# = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresPredictionsSeasonal where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, HeatScore from finishedContestScoresPredictionsDaily where cId = ? "
                       "order by HeatScore asc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, HeatScore from finishedContestScoresPredictionsWeekly where cId = ? "
                       "order by HeatScore asc",(cId))
        elif(duration == 'Seasonal'):
            cursor.execute("select userName, HeatScore from finishedContestScoresPredictionsSeasonal where cId = ? "
                       "order by HeatScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1] and streaks[0] > 2):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1 ,streaks[1]+1,streaks[1]+1, row[0]))
                elif (streaks[0] == streaks[1]):
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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesDaily where contest# = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesWeekly where contest# = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresExtremesSeasonal where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, ColdScore from finishedContestScoresExtremesDaily where contest# = ? "
                       "order by ColdScore desc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, ColdScore from finishedContestScoresExtremesWeekly where contest# = ? "
                       "order by ColdScore desc",(cId))
        else:
            cursor.execute("select userName, ColdScore from finishedContestScoresExtremesSeasonal where contest# = ? "
                       "order by ColdScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1] and streaks[0]):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1,streaks[1]+1,streaks[1]+1, row[0]))
                elif (streaks[0] == streaks[1] and streaks[0] > 2):
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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsDaily where cId = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsWeekly where cId = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresPredictionsSeasonal where cId = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, ColdScore from finishedContestScoresPredictionsDaily where cId = ? "
                       "order by ColdScore asc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, ColdScore from finishedContestScoresPredictionsWeekly where cId = ? "
                       "order by ColdScore asc",(cId))
        else:
            cursor.execute("select userName, ColdScore from finishedContestScoresPredictionsSeasonal where cId = ? "
                       "order by ColdScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1] and streaks[0] > 2):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1,streaks[1]+1,streaks[1]+1, row[0]))
                elif (streaks[0] == streaks[1]):
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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesDaily where contest# = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesWeekly where contest# = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresExtremesSeasonal where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, RainScore from finishedContestScoresExtremesDaily where contest# = ? "
                       "order by RainScore desc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, RainScore from finishedContestScoresExtremesWeekly where contest# = ? "
                       "order by RainScore desc",(cId))
        else:
            cursor.execute("select userName, RainScore from finishedContestScoresExtremesSeasonal where contest# = ? "
                       "order by RainScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1] and streaks[0] > 2):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1,streaks[1]+1,streaks[1]+1, row[0]))
                elif (streaks[0] == streaks[1]):
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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsDaily where cId = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsWeekly where cId = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresPredictionsSeasonal where cId = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, RainScore from finishedContestScoresPredictionsDaily where cId = ? "
                       "order by RainScore asc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, RainScore from finishedContestScoresPredictionsWeekly where cId = ? "
                       "order by RainScore asc",(cId))
        else:
            cursor.execute("select userName, RainScore from finishedContestScoresPredictionsSeasonal where cId = ? "
                       "order by RainScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1] and streaks[0] > 2):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1,streaks[1]+1,streaks[1]+1, row[0]))
                elif (streaks[0] == streaks[1]):
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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesDaily where contest# = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresExtremesWeekly where contest# = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresExtremesSeasonal where contest# = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, RainScore from finishedContestScoresExtremesDaily where contest# = ? "
                       "order by WindScore desc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, RainScore from finishedContestScoresExtremesWeekly where contest# = ? "
                       "order by WindScore desc",(cId))
        else:
            cursor.execute("select userName, RainScore from finishedContestScoresSeasonal where contest# = ? "
                       "order by WindScore desc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1] and streaks[0] > 2):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1,streaks[1]+1,streaks[1]+1, row[0]))
                elif (streaks[0] == streaks[1] and streaks[0] > 2):
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
        if(duration == 'Daily'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsDaily where cId = ?",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select count(userName) from finishedContestScoresPredictionsWeekly where cId = ?",(cId))
        else:
            cursor.execute("select count(userName) from finishedContestScoresPredictionsSeasonal where cId = ?",(cId))
        totalPlayers = cursor.fetchone()[0]
        prizePool = totalPlayers * price
        firstPrize = prizePool * .5
        secondPrize = prizePool * .3
        thirdPrize = prizePool * .2
        if(duration == 'Daily'):
            cursor.execute("select userName, WindScore from finishedContestScoresPredictionsDaily where cId = ? "
                       "order by WindScore asc",(cId))
        elif(duration == 'Weekly'):
            cursor.execute("select userName, WindScore from finishedContestScoresPredictionsWeekly where cId = ? "
                       "order by WindScore asc",(cId))
        else:
            cursor.execute("select userName, WindScore from finishedContestScoresPredictionsSeasonal where cId = ? "
                       "order by WindScore asc",(cId))
        values = cursor.fetchall()
        count = 0
        for row in values:
            if count == 0:
                cursor.execute("select currentStreak, maxStreak from history where userName = ?",(row[0]))
                streaks = cursor.fetchall()
                if (streaks[0] == streaks[1] and streaks[0] > 2):
                    cursor.execute("update history set earnings = earnings+?, currentStreak = ?, maxStreak = ?, "
                                   "gamesWon = gamesWon+1, totalGames=totalGames+1 where userName = ?",(firstPrize * 1.1,streaks[1]+1,streaks[1]+1, row[0]))
                elif (streaks[0] == streaks[1] and streaks[0] > 2):
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


