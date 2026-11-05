#erstellt mithilfe von KI, um die plausibilität der CAN-Daten zu überprüfen und in einer Streamlit-App anzuzeigen
import pandas as pd
import streamlit as st
from daten import Messungen
from funktionen import check_plausibilität, del_duplicates, print_messung

st.title("CAN-Datenanzeige")

#define acceptable ranges for each CAN message
plausible_ranges = {
    "steering_travel": (0, 100),
    "vehicle_speed": (0, 200),
    "wheel_rpm_fr": (0, 500),
    "wheel_rpm_fl": (0, 1000),
    "accumulator_SOC": (0, 100),
    }

#check each measurement for plausibility
plausible_data = []
for messung in Messungen:
    can_message = messung["CAN_Message"]
    value = messung["value"]
    if can_message in plausible_ranges:
        min_wert, max_wert = plausible_ranges[can_message]
        if min_wert <= value <= max_wert:
            plausible_data.append(messung)

#print the plausible data
if __name__== "__main__":
    for messung in plausible_data:
        print_messung(messung)

#display the  data in a Streamlit app 
if plausible_data:
    st.write("Wertebereiche für plausible Messungen:")
    st.dataframe(pd.DataFrame.from_dict(plausible_ranges, orient='index', columns=['min_wert', 'max_wert']))
    st.write("Die plausiblen Daten sind:")  
    st.dataframe(pd.DataFrame(plausible_data))
    st.write("Die nicht plausible Daten sind:")
    st.dataframe(pd.DataFrame([messung for messung in Messungen if messung not in plausible_data]))
