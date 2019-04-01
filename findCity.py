from geopy.geocoders import Nominatim
import overpy
import urllib.request as request
import json

def getCityName(coordinateX,coordinateY):
    '''

    :param coordinateX:
    :param coordinateY:
    :return: name of the city relating to the coordinates
    '''
    geolocator = Nominatim(user_agent="my-app")
    coord= str(coordinateX)+ ", " + str(coordinateY)
    location = geolocator.reverse(coord)

    try:
        res = location.raw['address']['city']
    except:
        try:
            res = location.raw['address']['town']
        except:
            res = None

    return res










def get_Id(nom):

    api = overpy.Overpass()

# We can also see a node's metadata:
# result = api.query("relation({}); out meta;")

    result = api.query("relation[name = "+ nom +"]; out meta;")

    res = result.get_relation_ids()[0] # return city list of the id
    return res
id = get_Id("Annemasse")
# print(id)

def get_center_coordinate(name):

    api = overpy.Overpass()
    # print(name)
# We can also see a node's metadata:
# result = api.query("relation({}); out meta;")
    try:
        result = api.query("relation[name = "+name+"]; out center meta;")
        res = [float(result.get_relation(result.get_relation_ids()[0]).center_lat),float(result.get_relation(result.get_relation_ids()[0]).center_lon)]
    except:
        res=None
    return res

def get_polygone(id):
    """

    :param id: the id of a city
    :return: dict of the polygone which represents the city
    """
    url="http://polygons.openstreetmap.fr/get_geojson.py?id="+str(id)+"&params=0"

    page = request.urlopen(url)
    data=page.read()
    encoding = page.info().get_content_charset('utf-8')
    j= json.loads(data.decode(encoding))
    return j["geometries"]

# print(get_polygone(104959))

