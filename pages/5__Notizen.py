import streamlit as st
import pandas as pd
from jsonbin import load_data, save_data

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


st.title("Notizen Auswertung")

file_notice=load_data(api_key, bin_id)
    
notice = "notice"
notes = [day[notice]for key, day in file_notice.items() if notice in day]   #getting values from nested dictionary


df = pd.DataFrame({
    "notice" : notes,
    "day" : file_notice.keys()
    })

st.dataframe(df, width=1024, height=768)
