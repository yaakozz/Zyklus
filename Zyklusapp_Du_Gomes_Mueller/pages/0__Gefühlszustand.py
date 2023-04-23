import streamlit as st
import pandas as pd
import altair as alt
import json


st.title("Gefühlszustand Auswertung")

#barchart with pandas for feelings
with open("data.json", "r")as file:
    file_feeling = json.load(file)


feel = "feeling"
feelings = [day[feel]for key, day in file_feeling.items() if feel in day]   #getting values from nested dictionary

dif = pd.DataFrame({
    "feeling" : feelings,
    "day" : file_feeling.keys()
    })

st.write("Gemessene Werte", feelings)

st.line_chart(dif, x= "day", y = "feeling")