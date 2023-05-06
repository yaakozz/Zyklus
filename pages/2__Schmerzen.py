import streamlit as st
import pandas as pd
import altair as alt
from jsonbin import load_data, save_data

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


st.title("Schmerzen Auswertung")

#barchart with pandas for pain

file_pain=load_data(api_key, bin_id)




pain = "pain"
pain_values = [day[pain]for key, day in file_pain.items() if pain in day]   #getting values from nested dictionary

dif = pd.DataFrame({
    "pain" : pain_values,
    "day" : file_pain.keys()
    })

st.write("Gemessene Werte", pain_values)

st.line_chart(dif, x= "day", y = "pain")


