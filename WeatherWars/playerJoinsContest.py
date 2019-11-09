import pyodbc

def playerJoinsContestExtremes(userName, teamName, cId, tenCities, cursor, conn):
    cursor.execute("select userName from buyInto where userName = ? and cId = ?",(userName, cId))
    if cursor.fetchone() == None:
        cursor.execute("insert into team values (?)", (teamName))
        cursor.execute("select max(tId) from team")
        tId = cursor.fetchone()[0]
        #print(tId)
        cursor.execute("insert into buyInto values (?,?,?)",(userName, cId, tId))
        
        for city in tenCities:
            cursor.execute("insert into comprisedOf values (?,?, NULL)", (tId, city))
    conn.commit()

