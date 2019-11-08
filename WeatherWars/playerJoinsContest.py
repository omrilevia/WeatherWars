import pyodbc

def playerJoinsContestExtremes(userName, teamName, cId, tenCities, cursor, conn):
    cursor.execute("select userName from buyInto where userName = ? and cId = ?",(userName, cId))
    if cursor.fetchone() == None:
        