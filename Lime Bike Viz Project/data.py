import requests as re 
import pandas as pd
import numpy as np
import json

url="https://web-production.lime.bike/api/rider/v1/views/map?ne_lat=39.74219108230314&ne_lng=-104.9658931419253&sw_lat=39.72879224618626&sw_lng=-104.97393976897&user_latitude=39.73504638671875&user_longitude=-104.9699164729487&zoom=16"

headers = {
    'Authorization': 'Bearer limebike-PMc3qGEtAAXqJa',
}

params = (
    ('region', 'Washington DC Proper'),
)

response = re.get('https://lime.bike/api/partners/v1/bikes', headers=headers, params=params)
data = json.loads(response.text)
data = (data['data'])
# print(data)
typeB = [data[0]['attributes']['vehicle_type']]
for i in range(1, len(data)):
    typeB.append(data[i]['attributes']['vehicle_type'])
latsS = pd.Series(data[0]['attributes']['latitude'])
longS = pd.Series(data[0]['attributes']['longitude'])
plateNumS = pd.Series(data[0]['attributes']['plate_number'])

for i in range(1, len(data)):
    latsS[i] = pd.Series(data[i]['attributes']['latitude'])
    longS[i] = pd.Series(data[i]['attributes']['longitude'])
    plateNumS[i] = pd.Series(data[i]['attributes']['plate_number'])

df = pd.DataFrame({
    "Type": typeB,
    "Latitude": latsS.astype('float'),
    "Longitude": longS.astype('float'),
    "Plate Number": plateNumS
}) 
df1 = df[df['Type'] == 'bike']
df2 = df[df['Type'] == 'scooter']

df1len = len(df1)
df1ALat = (np.average(df1["Latitude"]))
df1ALon = (np.average(df1["Longitude"]))

df2len = len(df2)
df2ALat = (np.average(df2["Latitude"]))
df2ALon = (np.average(df2["Longitude"]))
