import pymysql as pysql

def getConnection():
    db = pysql.connect( user='root',
                        password='',
                        host='localhost',
                        port=1234 )
    
    return db