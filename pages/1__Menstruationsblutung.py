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


st.title("Menstruationsblutung Auswertung")

#barchart with pandas for Menstruationblutung

file_intensity=load_key(api_key, bin_id, username)

df = pd.DataFrame(data)
df = df.melt(var_name='Index', value_name='Values')
df[['Date', 'Index']] = pd.DataFrame(df['Index'].tolist())

# Erstelle das Balkendiagramm
chart = alt.Chart(df).mark_bar().encode(
    x='Date',
    y='Values',
    color='Index',
    tooltip=['Date', 'Index', 'Values']
).properties(
    width=600,
    height=400
)

# Zeige das Balkendiagramm in Streamlit an
st.altair_chart(chart)

    
#intensity = "intensity"
#bleeding = [day[intensity]for key, day in file_intensity.items() if intensity in day]   #getting values from nested dictionary

    

#daf = pd.DataFrame({
 #   "intensity" : bleeding,
  #  "day" : file_intensity.keys()
   # })

st.write("Gemessene Werte", bleeding)


#bar_chart = alt.Chart(daf).mark_line().encode(
 #   x = "day",
  #  y = alt.Y("intensity", scale=alt.Scale(reverse=True)))

#st.altair_chart(bar_chart, use_container_width = True)
