import sqlite3
import datetime
from data import df1len, df1ALat, df1ALon, df2len, df2ALat, df2ALon
import pyproj

file = 'limebike.db'
time = datetime.datetime.now().isoformat() 

conn = sqlite3.connect(file) 
c = conn.cursor()

def initTable():
    c.execute(
        '''
        CREATE TABLE bikes (
            Amount INTEGER,
            LatitudeAverage REAL,
            LongitudeAverage REAL, 
            Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )
        '''
    )
    c.execute(
        '''
        CREATE TABLE scooters (
            Amount INTEGER,
            LatitudeAverage REAL,
            LongitudeAverage REAL, 
            Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )
        '''
    )

def add():
    c.execute(
        '''
        INSERT INTO bikes (
            Amount, 
            LatitudeAverage,
            LongitudeAverage, 
            Time
            )
        VALUES(?, ?, ?, ?)
        ''',(
            df1len, 
            df1ALat, 
            df1ALon, 
            time
        )
    )
    c.execute(
        '''
        INSERT INTO scooters (
            Amount, 
            LatitudeAverage,
            LongitudeAverage, 
            Time
            )
        VALUES(?, ?, ?, ?)
        ''',(
            df2len, 
            df2ALat, 
            df2ALon, 
            time
        )
    )
def getAllBikes():
    c.execute('''
        SELECT * FROM bikes
    ''')
    return(c.fetchall())

def getAllScooters():
    c.execute('''
        SELECT * FROM scooters
    ''')
    return(c.fetchall())


add()

def queryDistance():
    c.execute('''
        SELECT * FROM scooters
    ''')
    data = c.fetchall()
    for i in range(0, len(data)):
        if i == 0:
            continue
        else:
            lat1, long1 = (data[i][1], data[i][2])
            lat2, long2 = (data[i - 1][1], data[i - 1][2])

            geod = pyproj.Geod(ellps="WGS84")
            angle1, angle2, distance = geod.inv(long1, lat1, long2, lat2)

            print("Distance is {:0.2f} meters".format(distance))

queryDistance()

conn.commit()
conn.close()