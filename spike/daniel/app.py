import pandas as pd
import streamlit as st
from daten import MESSUNGEN
from funktionen import mittelwert_druck, anzahl_messungen, messtellen_darstellen

st.title("Spike: Testdaten")

average = st.slider("durschnittlicher Druck", min_value=0.900, max_value=1.300, value=1.020, step=0.001)

anzahl = anzahl_messungen(MESSUNGEN)
mittelwert = mittelwert_druck(MESSUNGEN)
messstellen = messtellen_darstellen(MESSUNGEN)

col1, col2 = st.columns(2)

with col1:
    st.metric("Anzahl Messungen", anzahl)

with col2:
    st.metric("durchschnittlicher Luftdruck", f"{mittelwert: .3f} hPa")

st.subheader("Messdaten")
df = pd.DataFrame(MESSUNGEN)
st.dataframe(df, use_container_width=True)

st.subheader("Druckeinstellung")
st.write(f"Ausgewählter Druck: {average: .3f} hPa")

