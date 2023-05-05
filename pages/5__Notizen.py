import streamlit as st
import pandas as pd
import json


st.title("Notizen Auswertung")

with open("data.json", "r")as file:
    file_notice = json.load(file)
    
notice = "notice"
notes = [day[notice]for key, day in file_notice.items() if notice in day]   #getting values from nested dictionary


df = pd.DataFrame({
    "notice" : notes,
    "day" : file_notice.keys()
    })

st.dataframe(df, width=1024, height=768)