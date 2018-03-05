import folium

my_map = folium.Map(location=[-1.363405, 36.933671], zoom_start=10.7)

fg = folium.FeatureGroup(name="My Features")
fg.add_child(folium.Marker(location=[-1.363405, 36.9336700006], 
               popup="Syokimau Home", icon=folium.Icon(color="red")))

locations = {"Gateway Mall" : [-1.364043, 36.912180],
             "Nextgen Mall" : [-1.323509, 36.844368],
             "Panari" : [-1.328665, 36.855907],
             "Imax" : [-1.282269, 36.822918]}

for location_name, location_cordinate in locations.items():
    fg.add_child(folium.Marker(location=location_cordinate, 
               popup=location_name, icon=folium.Icon(color="green")))


my_map.add_child(fg)

my_map.save("My_Map.html")
