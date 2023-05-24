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



st.title("Schmerzen Auswertung")

#barchart with pandas for pain

file_pain=load_key(api_key, bin_id, username)

Leer={}
for key in file_pain:
    Leer.update(key)
file_pain=Leer


pain = "pain"
pain_values = [day[pain]for key, day in file_pain.items() if pain in day]   #getting values from nested dictionary

dif = pd.DataFrame({
    "pain" : pain_values,
    "day" : file_pain.keys()
    })

#st.write("Gemessene Werte", pain_values)

st.line_chart(dif, x= "day", y = "pain")


