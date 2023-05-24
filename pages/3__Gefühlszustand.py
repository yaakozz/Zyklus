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



st.title("Gefühlszustand Auswertung")

#barchart with pandas for feelings

file_feeling=load_key(api_key, bin_id, username)

Leer={}
for key in file_feeling:
    Leer.update(key)
file_feeling=Leer

feel = "feeling"
feelings = [day[feel]for key, day in file_feeling.items() if feel in day]   #getting values from nested dictionary

dif = pd.DataFrame({
    "feeling" : feelings,
    "day" : file_feeling.keys()
    })

#st.write("Gemessene Werte", feelings)

st.line_chart(dif, x= "day", y = "feeling")
