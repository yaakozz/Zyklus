import streamlit as st
import pandas as pd
import altair as alt
from jsonbin import load_data, save_data

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]


st.title("Ovulationstest Auswertung")

#barchart with pandas for Ovutest

file_ovutest=load_data(api_key, bin_id)
    
ovu = "ovutest"
ovutests = [day[ovu]for key, day in file_ovutest.items() if ovu in day]   #getting values from nested dictionary
    
#sorting out all none ovutest
def ovu_not_none(ovutests):
    measured_ovutests = []
    for a in ovutests:
        if a != "Positiv" or "Negativ":
            measured_ovutests.append(a)
    return measured_ovutests

measured_ovu = ovu_not_none(ovutests)

daf = pd.DataFrame({
    "ovutest" : measured_ovu,
    "day" : file_ovutest.keys()
    })

st.write("Gemessene Werte", measured_ovu)

bar_chart = alt.Chart(daf).mark_bar().encode(
    x = "day",
    y = alt.Y("ovutest", scale=alt.Scale(reverse=True)))

st.altair_chart(bar_chart, use_container_width = True)
