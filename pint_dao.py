# Adapted code from lecture notes 'Topic06-data-layer/zstudentDAO.py
# Create table added from lecture create table notes

import mysql.connector

class PintDAO:
    host =""
    user = ""
    password =""
    database =""

    connection = ""
    cursor =""

    def __init__(self): 
        #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="pintsdb"
    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    
    # create table
    def create_table(self):
        cursor = self.getCursor()
        sql="""
        CREATE TABLE IF NOT EXISTS pint (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pub_name VARCHAR(100),
            price FLOAT
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

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from pint where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)
    
    def create(self, pint):
        cursor = self.getCursor()
        sql="insert into pint (pub_name, price) values (%s,%s)"
        values = (pint.get("pub_name"), pint.get("price"))
        cursor.execute(sql, values )

        self.connection.commit()
        newid = cursor.lastrowid
        pint["id"] = newid
        self.closeAll()
        return pint


    def update(self, id, pint):
        cursor = self.getCursor()
        sql="update pint set pub_name= %s, price=%s where id = %s"
    
        values = (pint.get("pub_name"), pint.get("price"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        
        self.closeAll()
        return pint

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from pint where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        return True

    def convertToDict(self,resultLine):
        pintKeys = ["id", "pub_name", "price"]
        currentkey = 0
        pint = {}
        for attrib in resultLine:
            pint[pintKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return pint


pintDAO = PintDAO()

























































