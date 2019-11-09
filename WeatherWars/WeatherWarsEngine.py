from contestManager import dailyContestHeatExtremes
from contestManager import dailyContestHeatPredictions
from contestManager import dailyContestColdExtremes
from contestManager import dailyContestColdPredictions
from contestManager import dailyContestRainExtremes
from contestManager import dailyContestRainPredictions
from contestManager import dailyContestWindExtremes
from contestManager import dailyContestWindPredictions
from contestManager import updateContestsAndCreateNew
from updatePlayerHistory import updatePlayerHistory
from fetchWeatherData import fetchWeatherData
from populateCities import populateCities
from newPlayer import addNewPlayer
from playerJoinsContest import playerJoinsContestExtremes
import pyodbc
import requests

def main():
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=LAPTOP-RC2ANL8F\SQLEXPRESS;'
                      'Database=WeatherWars;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    #populateCities(conn,cursor)
    fetchWeatherData(conn, cursor)
    updateContestsAndCreateNew(conn,cursor)
    playerOne = ['playerOne', 'password','11-15-1995','playerOne@gmail.com','4081111111']
    playerTwo = ['bigChungus', 'password','11-15-1995','chungus@gmail.com','9501231324']
    playerThree = ['chigBungus', 'password','2-12-1996','three@gmail.com', '4087335228']
    playerFour = ['notABot', 'password', '1-1-1980', 'four@gmail.com','1234567890']
    playerInfo = [playerOne,playerTwo,playerThree,playerFour]
    addNewPlayer(playerInfo,conn,cursor)
    tenCities = ['New York', 'Seattle', 'San Jose', 'Phoenix', 'Las Vegas', 'Honolulu', 'Atlanta', 'Boulder', 'Boston', 'Miami']
    playerJoinsContestExtremes('playerOne', 'aTeam', 0, tenCities, cursor, conn)
    

if __name__ == "__main__":
    main()
