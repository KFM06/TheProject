import streamlit as st
import folium
from streamlit_folium import st_folium
st.title('Map Test')
m = folium.Map(location=[49.1852, -57.4184], zoom_start=12)
# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
st_map(result) = st_folium(map)
