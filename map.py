import folium

#Creating the map object
m = folium.Map(location=[49.1852, -57.4184], zoom_start=12)

#Generating the map
m.save('map.html')