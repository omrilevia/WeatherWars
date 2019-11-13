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
from playerJoinsContest import playerJoinsContestPredictions
import pyodbc
import requests

def main():
    conn = pyodbc.connect("DRIVER={MySQL ODBC 8.0 Unicode Driver};user=root;password=Ankit6131;database=WeatherWars;")
    cursor = conn.cursor()
    populateCities(conn,cursor)
    fetchWeatherData(conn, cursor)
    updateContestsAndCreateNew(conn,cursor)
    playerOne = ['playerOne', 'password','1995-11-15','playerOne@gmail.com','4081111111']
    playerTwo = ['bigChungus', 'password','1995-11-15','chungus@gmail.com','9501231324']
    playerThree = ['chigBungus', 'password','1996-11-2','three@gmail.com', '4087335228']
    playerFour = ['notABot', 'password', '1980-1-1', 'four@gmail.com','1234567890']
    playerInfo = [playerOne,playerTwo,playerThree,playerFour]
    addNewPlayer(playerInfo,conn,cursor)
    tenCities = {'New York':40, 'Seattle':50, 'San Jose':75, 'Phoenix':80, 'Las Vegas':80, 'Honolulu':80, 'Atlanta':65, 'Boulder':70, 'Boston':35, 'Miami':69}
    #playerJoinsContestExtremes('playerOne', 'aTeam', 0, tenCities, cursor, conn)
    playerJoinsContestPredictions('playerOne', 'aTeam', 9, tenCities, cursor, conn)

if __name__ == "__main__":
    main()
