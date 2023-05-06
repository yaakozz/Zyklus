import streamlit as st
import pandas as pd
import altair as alt
from jsonbin import load_data, save_data

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


st.title("Temperatur Auswertung")

#bar chart for temperature

file_temperature=load_data(api_key, bin_id)
        
    #all measured Temperatures
temp = "temperatur"
temperatures = [day[temp]for key, day in file_temperature.items() if temp in day]   #getting values from nested dictionary

#sorting out all empty temperature inputs
def temp_not_none(temperatures):
    measured_temperatures = []
    for i in temperatures:
        if i != "":
            measured_temperatures.append(i)
    return measured_temperatures


df = pd.DataFrame({
    "temperatur" : temperatures,
    "day": file_temperature.keys()
})

st.write("Gemessene Werte", temp_not_none(temperatures))


bar_chart = alt.Chart(df).mark_bar().encode(
        y='temperatur',
        x='day',
    )
 
st.altair_chart(bar_chart, use_container_width=True)
