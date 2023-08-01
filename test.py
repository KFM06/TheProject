import streamlit as st
import folium
map = folium.Map()
m = folium.Map(location=[49.1852, -57.4184], zoom_start=12)
st.title('Map Test')
result = st.button('Click to view map')
st_map(result) = st_folium(map)
if result:
  st_map
