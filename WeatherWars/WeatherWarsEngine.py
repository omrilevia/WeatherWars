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
from contestManager import dailyContest
import pyodbc
import requests

def main():
    conn = pyodbc.connect("DRIVER={MySQL ODBC 8.0 Unicode Driver};user=root;password=Ankit6131;database=WeatherWars;")
    cursor = conn.cursor()
    populateCities(conn,cursor)
    fetchWeatherData(conn, cursor)
    updateContestsAndCreateNew(conn,cursor)
    
    

if __name__ == "__main__":
    main()
