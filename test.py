import streamlit as st
import folium
m = folium.Map(location=[49.1852, -57.4184], zoom_start=12)
st.title('Map Test')
result = st.button('Click to view map')
if result:
  m.save('map.html')
