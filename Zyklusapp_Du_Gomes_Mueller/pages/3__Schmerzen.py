import streamlit as st
import pandas as pd
import altair as alt
import json


st.title("Schmerzen Auswertung")

#barchart with pandas for pain
with open("data.json", "r")as file:
    file_pain = json.load(file)


pain = "pain"
pain_values = [day[pain]for key, day in file_pain.items() if pain in day]   #getting values from nested dictionary

dif = pd.DataFrame({
    "pain" : pain_values,
    "day" : file_pain.keys()
    })

st.write("Gemessene Werte", pain_values)

st.line_chart(dif, x= "day", y = "pain")