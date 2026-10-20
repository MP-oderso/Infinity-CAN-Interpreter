import pandas as pd
import streamlit as st
from daten import messungen

st.title("Messungen Übersicht")
st.write("Hier sind die Messungen an verschiedenen Orten:")

daten = st.slider("Wählen Sie die Anzahl der Messungen aus:", min_value=1, max_value=len(messungen), value=len(messungen))

for i in range(daten):
    messung = messungen[i]
    st.write(f"Messung an {messung['data']}: x1={messung['x1']}, x2={messung['x2']}, x3={messung['x3']}")

tabelle = pd.DataFrame(messungen)
st.write("Tabelle der Messungen:")
st.dataframe(tabelle)

st.write("Karte der Messungen:")
messungen_koordinaten = [{"data": "ort1", "latitude": st.slider("Latitude", min_value=0.0, max_value=90.0, value=52.5200), "longitude": st.slider("Longitude", min_value=-180.0, max_value=180.0, value=13.4050)},
                        {"data": "ort2", "latitude": st.slider("Latitude", min_value=0.0, max_value=90.0, value=48.8566), "longitude": st.slider("Longitude", min_value=-180.0, max_value=180.0, value=2.3522)},
                        {"data": "ort3", "latitude": st.slider("Latitude", min_value=0.0, max_value=90.0, value=51.5074), "longitude": st.slider("Longitude", min_value=-180.0, max_value=180.0, value=-0.1278)}]
st.map(pd.DataFrame(messungen_koordinaten))  # Zeigt die Messungen auf einer Karte an, falls Koordinaten vorhanden sind
