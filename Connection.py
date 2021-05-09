import pymysql as pysql

def getConnection():
    db = pysql.connect( user='root',
                        password='',
                        host='localhost',
                        port=3306 )
    
    return db
