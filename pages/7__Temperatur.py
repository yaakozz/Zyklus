import streamlit as st
import pandas as pd
import altair as alt
import json


st.title("Temperatur Auswertung")

#bar chart for temperature

with open("data.json", "r") as file:
    file_temperature = json.load(file)
        
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
