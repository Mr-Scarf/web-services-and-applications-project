# PintDAO - Dat access Object for pints app.
# Adapted code from lecture notes 'Topic 06 : Data-layer (studentDAO.py) & Topic 11 :  SQLite3 and pythonanywhere
# Create table added from lecture create table notes
# Used chatpgt to assist with adding timestamps for creation or updates of pints data - https://chatgpt.com/share/69ff38db-0394-832e-81aa-e3e657374f56

import sqlite3
from datetime import datetime


class PintDAO:
    #host =""  
    #user = ""
    #password =""
    #database =""

    connection = ""
    cursor =""

    #def __init__(self): 
        #these should be read from a config file
        #self.host="localhost"
        #self.user="root"
        #self.password=""
        #self.database="pintsdb"
    
    def getCursor(self): 
        self.connection = sqlite3.connect("pints.db")
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.cursor.close()
        self.connection.close()
        
    
    
    # create table
    def create_table(self):
        cursor = self.getCursor()
        sql="""
        CREATE TABLE IF NOT EXISTS pint (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pub_name TEXT,
            price REAL,
            created_at TEXT,
            updated_at TEXT
        )
        """
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()
    
 
    def getAll(self):
        cursor = self.getCursor()
        sql="select * from pint"
        cursor.execute(sql)
        result = cursor.fetchall()
        pintlist = []
        for row in result:
            pintlist.append(self.convertToDict(row))

        self.closeAll()
        return pintlist
 # fIND BY ID  
    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from pint where id = ?"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)
  #Create  
    def create(self, pint):
        cursor = self.getCursor()

        now = datetime.now().isoformat()

        sql="insert into pint (pub_name, price , created_at, updated_at) values (?,?,?,?)" # Add timestamp
        values = (pint.get("pub_name"), pint.get("price"),now, now)
        cursor.execute(sql, values )

        self.connection.commit()
        newid = cursor.lastrowid
        pint["id"] = newid
        pint["created_at"] = now # Add timestamp
        pint["updated_at"] = now # Add timestamp
        self.closeAll()
        return pint

    #Update
    def update(self, id, pint):
        cursor = self.getCursor()

        now = datetime.now().isoformat()

        sql="update pint set pub_name= ?, price=?, updated_at = ? where id = ?"
    
        values = (pint.get("pub_name"), pint.get("price"), now, id)
        cursor.execute(sql, values)
        self.connection.commit()
        
        self.closeAll()
        pint["id"] = id
        pint["updated_at"] = now

        return pint
    
    #Delete
    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from pint where id = ?"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        return True

    def convertToDict(self,resultLine):
        if resultLine is None:
            return None
        
        pintKeys = ["id", "pub_name", "price", "created_at", "updated_at"]
         
        return dict(zip(pintKeys, resultLine))


pintDAO = PintDAO()

























































