import streamlit as st
from datetime import datetime, date, timedelta 
import json

st.title("Zyklusapp")

#Zyklusrechner

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


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

#Hauptteil der App, Eingabe der Beschwerden
col1, col2, col3 = st.columns(3)

with col1:
    feeling = st.radio(
        "Wie fühlst du dich?", 
        ("😀", "😐", "😭", "😡"))

with col2:
    intensity = st.radio(
        "Wie stark sind die Menstruationsblutungen?",
        ("Keine","Leicht", "Mittel", "Stark"))
    
with col3:    
    notice= st.text_area(
        "Meine Notizen:")
    

    
col4, col5 = st.columns(2)

with col4:
    ovutest = st.radio(
        "Habe ich einen Ovulationstest gemacht? Wenn ja, was war das Resultat?", 
        ("Keinen Test gemacht", "Positiv", "Negativ"))

with col5:
    temperatur= st.text_input(
        "Meine gemessene Temperatur in °C:",
        "")
    

def save():
    
    
    with open('data.json','r') as file:
        data=json.load(file)
    
    data.update({
            str(date): {
                'pain': pain, 
                'feeling': feeling,
                'intensity': intensity,
                'notice': notice,
                'ovutest': ovutest,
                'temperatur': temperatur
            }
        })
    
    #st.write(data)
    with open('data.json','w') as file:
        json.dump(data,file,indent=4)
        
        
           
    return 
button = st.button('Speichern',on_click=save)