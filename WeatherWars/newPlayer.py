import pyodbc

def addNewPlayer(playerInfo, conn, cursor):
    for row in playerInfo:
        cursor.execute("select userName from player where userName = ?",(row[0]))
        value = cursor.fetchone()
        if value == None:
            cursor.execute("insert into player values (?,?,?,?,?)", (row[0],row[1],row[2],row[3],row[4]))
            cursor.execute("insert into history values (?,?,?,?,?,?)",(row[0],0,0,0,0,0))
    conn.commit()