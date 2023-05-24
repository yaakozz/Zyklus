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


st.title("Temperatur Auswertung")

#bar chart for temperature

file_temperature=load_key(api_key, bin_id, username)

Leer={}
for key in file_temperatur:
    Leer.update(key)
file_temperatur=Leer
        
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

#st.write("Gemessene Werte", temp_not_none(temperatures))


bar_chart = alt.Chart(df).mark_bar().encode(
        y='temperatur',
        x='day',
    )
 
st.altair_chart(bar_chart, use_container_width=True)
