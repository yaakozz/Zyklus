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


#Dataframe with pandas for medis

file_medi1=load_key(api_key, bin_id, username)
#st.write(file_medi1)
#dfML=pd.DataFrame(file_medi1)
#st.dataframe(dfML)


medi1 = "medi1"
Morgen = [day[medi1]for key, day in file_medi1.items() if medi1 in day]     #getting values from nested dictionary

medi2 = "medi2"
Mittag = [day[medi2]for key, day in file_medi1.items() if medi2 in day]

medi3 = "medi3"
Abend = [day[medi3]for key, day in file_medi1.items() if medi3 in day]

medi4 = "medi4"
Schlafen = [day[medi4]for key, day in file_medi1.items() if medi4 in day]

Tag = file_medi1.keys()

#taken_medi = dict((k, eval(k)) for k in ("Morgen", "Mittag", "Abend", "Schlafen", "Tag"))     #creating dictionary for panda dataframe

#df = pd.DataFrame.from_dict(taken_medi, orient = "index", columns=['values'])
#st.dataframe(df, width=1024, height=768)
