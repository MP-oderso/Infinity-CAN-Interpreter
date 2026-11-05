import pandas as pd
import streamlit as st
from daten import MESSUNGEN
from funktionen import filternmin, filternmax, mittelwert

st.title("Akkustack Temperaturen")
st.subheader("Erster Spike mit noch ausgedachten Temperaturen")
#minimum = st.slider("Mindesttemperatur", -10.0, 30.0, 0.0)
minimum = st.number_input(label="Mindesttemperatur",value=20.0, min_value=10.0, max_value=50.0)
maximum = st.number_input(label="Maximaltemperatur",value=60.0, min_value=10.0, max_value=80.0)
auswahlmin = filternmin(MESSUNGEN, "min-temp", minimum)
auswahlmax = filternmax(MESSUNGEN, "max-temp", maximum)
auswahl = [x for x in auswahlmin if x in auswahlmax]
critlow = [x for x in MESSUNGEN if x not in auswahlmin]
crithigh = [x for x in MESSUNGEN if x not in auswahlmax]

if crithigh:
    st.error("Kritisch hohe Temperatur")
    st.metric("Anzahl", len(crithigh))
    tabelle3 = pd.DataFrame(crithigh)
    tabelle3.index+=1
    st.dataframe(tabelle3.rename(columns={"akkustack": "Akkustack", "min-temp": "kleinste gemessene Temperatur", "max-temp": "höchste gemessene Temperatur", "avg-temp": "Durchschnittsemperatur"}))   
    
if auswahl:
    st.subheader("Normbereich")
    st.metric("Anzahl im Normbereich", len(auswahl))
    st.metric("Durchschnittsdurchschnittstemperatur", f"{mittelwert(auswahl, 'min-temp'):.1f} °C")
    tabelle1 = pd.DataFrame(auswahl)
    tabelle1.index+=1
    st.dataframe(tabelle1.rename(columns={"akkustack": "Akkustack", "min-temp": "kleinste gemessene Temperatur", "max-temp": "höchste gemessene Temperatur", "avg-temp": "Durchschnittsemperatur"}))

if critlow:
    st.subheader("Zu niedrige Temperatur")
    st.metric("Anzahl", len(critlow))
    st.write("bei folgenden Stacks Temperaturfühler kontrollieren")
    tabelle2 = pd.DataFrame(critlow)
    tabelle2.index+=1
    st.dataframe(tabelle2.rename(columns={"akkustack": "Akkustack", "min-temp": "kleinste gemessene Temperatur", "max-temp": "höchste gemessene Temperatur", "avg-temp": "Durchschnittsemperatur"}))