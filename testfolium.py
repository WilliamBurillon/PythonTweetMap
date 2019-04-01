try:
    import json
except ImportError:
    import simplejson as json
import mysql.connector
import folium

from TP1 import findCity as fC






# Connection in the database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="tweepy")
mycursor =mydb.cursor()

# get the coordinates in the tweets tables
mycursor.execute('''SELECT id,`position_X`,`position_Y` FROM `tweets`''')

# use the folium package to make the map and add points relating to the coordinates of the tweets
fond = r'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
carte = folium.Map(location=[46.5, 2.3], zoom_start=6, tiles=fond, attr='© OpenStreetMap © CartoDB')


for row in mycursor:

    # loop to put the tweet at the location where it was generate
    # carte.add_child(folium.Marker(location=[float(row[1]), float(row[2])]))

    #loop to put the tweet in the center of the city where it was generate
    city_name =fC.getCityName(float(row[1]),float(row[2]))
    print(city_name)
    center_coordinate = fC.get_center_coordinate(city_name)
    if center_coordinate == None:

        carte.add_child(folium.Marker(location=[float(row[1]), float(row[2])]))
    else:


        carte.add_child(folium.Marker(location=center_coordinate))


carte.save(outfile='map2.html')
