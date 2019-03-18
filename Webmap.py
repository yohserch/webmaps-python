from folium import Map, Icon, FeatureGroup, CircleMarker, GeoJson, LayerControl
import pandas


data = pandas.read_csv("Volcanoes.csv")

lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, long, elev):
    fgv.add_child(CircleMarker(location=[lt, ln], radius=6, popup=str(el), fill=True,
                              color=color_producer(el), fill_opacity=1))

fgp = FeatureGroup(name="Population")

fgp.add_child(GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(LayerControl())

map.save("Map1.html")