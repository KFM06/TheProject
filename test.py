import folium
from streamlit_folium import st_folium, folium_static

m = folium.Map(location=[49.1852, -57.4184], 
                 zoom_start=3, control_scale=True)

#Loop through each row in the dataframe
for i,row in df.iterrows():
    #Setup the content of the popup
    iframe = folium.IFrame('Well Name:' + str(row["Well Name"]))
    
    #Initialise the popup using the iframe
    popup = folium.Popup(iframe, min_width=300, max_width=300)
    
    #Add each row to the map
    folium.Marker(location=[row[49.1852],row[-57.4184]],
                  popup = popup, c=row['Well Name']).add_to(m)

st_data = folium_static(m, width=700)
