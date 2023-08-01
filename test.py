import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[49.1852, -57.4184], zoom_start=16)
folium.Marker(
    [49.1852, -57.4184], popup="Deer Lake", tooltip="Deer Lake"
).add_to(m)

# call to render Folium map in Streamlit, but don't get any data back
# from the map (so that it won't rerun the app when the user interacts)
st_folium(m, width=725, returned_objects=[])
