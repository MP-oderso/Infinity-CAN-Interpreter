#Python üben Grundlagen

import streamlit as st
import pandas as pd
# mit KI
import folium
from wetterdienst import Wetterdienst
from streamlit_folium import st_folium
# bis hier

st.title("Wetter am Niederrhein")
st.write("Live-Demo: Python-grundlagen in einer kleinen Web-App")
st.subheader("Zufällige Daten:")

st.sidebar.header("Cofiguration")
name = st.sidebar.text_input("Your name", value="Marcus")
num_rows = st.sidebar.slider("Number of rows", min_value=5, max_value=100, value=20)
st.sidebar.subheader("Wetter")
st.sidebar.write("Map-Configuration")
st.sidebar.caption("Dataset for the map: DWD")



# Generate sample data
data = pd.DataFrame({
    "Category": [f"Item {i}" for i in range(num_rows)],
    "Value": [i * 3.14 for i in range(num_rows)],
    "Status": ["Active" if i % 2 == 0 else "Inactive" for i in range(num_rows)]
})
 
# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Items", len(data))
col2.metric("Active", len(data[data["Status"] == "Active"]))
col3.metric("Average Value", f"{data['Value'].mean():.2f}")
 
# Display the dataframe
st.dataframe(data, use_container_width=True)
st.write(f"zufällige Daten generiert durch Code von {name}!")
 
# Simple chart
st.line_chart(data.set_index("Category")["Value"])

# ki unterstützung
api = Wetterdienst(provider="dwd", network="observation")

request = api(
    parameters=[("daily", "climate_summary")],
    periods=["historical"],
)

stations = request.all()
df = stations.df

karte = folium.Map(
    location=[51.7083, 6.1644],  # Pfalzdorf NRW
    zoom_start=6,
)

for station in df.iter_rows(named=True):
    folium.Marker(
        location=[station["latitude"], station["longitude"]],
        tooltip=station["name"],
        popup=f"{station['name']}: {station['elevation']} m",
    ).add_to(karte)

st_folium(karte, width=700, height=500)
