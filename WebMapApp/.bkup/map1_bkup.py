import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_prod(ele):
    if ele < 1000:
        return 'green'
    elif 1000<= ele <= 3000:
        return 'orange'
    else:
        return 'red'


#map.add_child(folium.Marker(location=[38.2,-99.1],popup="Marker here",icon=folium.Icon(color='red')))

"""
populating Markers with seprate code
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Marker here",icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[37.2,-100.1],popup="Marker here",icon=folium.Icon(color='blue')))
"""

# populating Markers with For Loop

map = folium.Map(location=[38.58, -99.28],zoom_start=8, tiles="Stamen Terrain")

#for Volcano
fgv = folium.FeatureGroup(name="Volcanoes")

"""[point populating via manula input]

for cordinates in [[38.2,-99.56],[39.5,-100.62]]:
    fg.add_child(folium.Marker(location=cordinates,popup="Marker here",icon=folium.Icon(color='red')))
    """

# adding points from Files
"""
for lt ,ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln],
                               popup="elevation : "+str(el)+"m.", icon=folium.Icon(color='red')))
"""
"""[POPUP] update
        if there are "" in any data, you will get blank page to update this use 

        popup = folium.Popup(str(el)),parse_html=True
    """

#for dynamic color binding

#for infosign marker

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln],
                               popup="elevation : "+str(el)+"m.", icon=folium.Icon(color=color_prod(el))))

"""
#for circle marker
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup="elevation : "+str(el)+"m."
        ,color='grey',fill=True, fill_opacity=0.7, icon=folium.Icon(color=color_prod(el))))
"""

#adding jeoJason

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))



map.add_child(fgv)
map.add_child(fgp)


#Layer Control
map.add_child(folium.LayerControl())

map.save("Map1.html")
