import altair as alt
import streamlit as st
from datetime import datetime, date, timedelta 
from jsonbin import load_key, save_key     #from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import pandas as pd

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]

# -------- user login --------
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == True:   # login successful
    authenticator.logout('Logout', 'main')   # show logout button
elif authentication_status == False:
    st.error('Username/password is incorrect')
    st.stop()
elif authentication_status == None:
    st.warning('Please enter your username and password')
    st.stop()

st.title("Ovulationstest Auswertung")

#barchart with pandas for Ovutest

file_ovutest=load_key(api_key, bin_id, username)

Leer={}
for key in file_ovutest:
    Leer.update(key)
file_ovutest=Leer
    
    
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

#st.write("Gemessene Werte", measured_ovu)

bar_chart = alt.Chart(daf).mark_bar().encode(
    x = "day",
    y = alt.Y("ovutest", scale=alt.Scale(reverse=True)))

st.altair_chart(bar_chart, use_container_width = True)
