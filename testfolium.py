try:
    import json
except ImportError:
    import simplejson as json
import mysql.connector

import folium

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="tweepy")
mycursor =mydb.cursor()
mycursor.execute('''SELECT id,`position_X`,`position_Y` FROM `tweets`''')

# for row in mycursor:
#     print(type(row[1])





#
fond = r'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
carte = folium.Map(location=[46.5, 2.3], zoom_start=6, tiles=fond, attr='© OpenStreetMap © CartoDB')

# fg=folium.FeatureGroup(name="tweet")

for row in mycursor:
    carte.add_child(folium.Marker(location=[float(row[1]), float(row[2])]))
# carte.add_child(folium.Marker(location=[6.14,45.9]))
carte.save(outfile='map.html')
