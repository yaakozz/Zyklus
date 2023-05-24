import streamlit as st
from datetime import datetime, date, timedelta 
from jsonbin import load_data, save_data     #from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]

# -------- user login --------
with open('config.yaml') as file:
    #config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
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



st.title("Zyklusapp")


#date input on calendar
date = st.date_input( 
    "Wann war mein letzter Zyklus?",
    date.today())

#ISO date to european date
european_format = "%d.%m.%Y"            
st.write('Letzter Zyklus war am:', datetime.strftime(date, european_format))

#next menstruation date calculated
next_date = date + timedelta(days=28)
st.write("Nächster Zyklus ist am", datetime.strftime(next_date, european_format))




#Eingabe Stärke der Schmerzen
pain = st.slider('Wie stark sind deine Schmerzen? 1 schwach und 10 stark', 0, 10)
st.write("Sie haben eine Stärke von", pain)

st.text("Ich habe heute folgende Medikamente genommen:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    medi1 = st.selectbox(
        "Morgen",
        ("Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
        )
    
with col2:
    medi2 = st.selectbox(
        "Mittag",
        ("Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
        )
    
with col3:
     medi3 = st.selectbox(
         "Abend",
         ("Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
         )

with col4:
    medi4 = st.selectbox(
        "Vor dem Schlafen",
        ("Paracetamol", "Ibuprofen", "Acetylsalicylsäure", "Naproxen", "Diclofenac")
        )
    

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

#Hauptteil der App, Eingabe der Beschwerden
col5, col6, col7 = st.columns(3)

with col5:
    feeling = st.radio(
        "Wie fühlst du dich?", 
        ("😀", "😐", "😭", "😡"))

with col6:
    intensity = st.radio(
        "Wie stark sind die Menstruationsblutungen?",
        ("Keine","Leicht", "Mittel", "Stark"))
    
with col7:    
    notice= st.text_area(
        "Meine Notizen:")
    

    
col8, col9 = st.columns(2)

with col8:
    ovutest = st.radio(
        "Habe ich einen Ovulationstest gemacht? Wenn ja, was war das Resultat?", 
        ("Keinen Test gemacht", "Positiv", "Negativ"))

with col9:
    temperatur= st.text_input(
        "Meine gemessene Temperatur in °C:",
        "")
    

def save():
    
    
    data=load_data(api_key, bin_id) #load_key(api_key, bin_id, key, empty_value=[])





 
    data.update({
            str(date): {
                'pain': pain,
                'medi1': medi1,
                'medi2': medi2,
                'medi3': medi3,
                'medi4': medi4,
                'feeling': feeling,
                'intensity': intensity,
                'notice': notice,
                'ovutest': ovutest,
                'temperatur': temperatur
            }
        })
  

    save_data(api_key, bin_id, data)  #save_key(api_key, bin_id, key, data)






        
           
    return 
button = st.button('Speichern',on_click=save)

# Test


# -------- user login --------
#with open('config.yaml') as file:
    #config = yaml.load(file, Loader=SafeLoader)

#authenticator = stauth.Authenticate(
    #config['credentials'],
    #config['cookie']['name'],
    #config['cookie']['key'],
    #config['cookie']['expiry_days'],
    #config['preauthorized']
#)

#name, authentication_status, username = authenticator.login('Login', 'main')

#if authentication_status == True:   # login successful
    #authenticator.logout('Logout', 'main')   # show logout button
#elif authentication_status == False:
    #st.error('Username/password is incorrect')
    #st.stop()
#elif authentication_status == None:
    #st.warning('Please enter your username and password')
    #st.stop()





