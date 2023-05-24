import streamlit as st
from datetime import datetime, date, timedelta 
from jsonbin import load_key, save_key     #from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

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


st.title("Tipps rund um den Zyklus")

st.write("Oftmals ist der Zyklus mit lästigen Symptomen, wie Stimmungsschwankungen, Schmerzen und weitere Beschwerden verbunden. " 
         "Dieser Teil der App ist dazu da, um bei der Linderung von diesen Symptomen zu helfen")

st.subheader("Schmerzen")
st.write("Um die Schmerzen zu lindern, gibt es verschiedene Möglichkeiten, wie Wärme, Bewegung und Schmerzmittel. "
         "Wichtig ist dabei die Methode zu finden die für einem selber am besten passt und nützt.")

st.write("-Wärme: Hilft die Muskeln zu entspannen. "
         " Die Möglichkeiten, die es gibt sind: Bettflaschen, Wärmepflaster und warme Duschen oder warme Bäder")

st.write("-Schmerzmittel: Schmerzmittel können für viele Arten von Schmerzen eingsetz werden." 
        " Je nach Verträglichkeit gibt es auch verschieden Wirkstoffe, die eingesetzt werden können." 
        " Einige Wirkstoffe sind:") 
st.write("-Paracetamol: wirkt schmerzstillend und fiebersenkend")
st.write("-Ibuprofen: wirkt schmerzstillend, fiebersenkend und entzündungshemmend")
st.write("-Acetylsalicylsäure: hat die gleiche Wirkung wie Ibuprofen, wird aber nicht oft empfohlen wegen den Nebenwirkungen")
st.write("-Naproxen: hat eine stärkere Wirkung im Gegensatz zu den anderen Schmerzmittel")
st.write("-Diclofenac: hat die gleiche Wirkung wie Ibuprofen.")

st.markdown(":red[Achtung: Paracetamol verträgt sich gut mit den anderen Schmerzmittel, aber die anderen vertragen sich nicht gegenseitig!]")

st.subheader("Stimmungsschwankungen")
st.write("Gegen Stimmungsschwankungen kann spezifisch nicht viel gemacht werden." 
         " Was gegen allgemeine Prämenstruelle Symptome, auch PMS genannt gemacht werden kann, ist Mönchspfeffer zu nehmen."
         " Mönchspfeffer hilft bei der stabilisierung von Hormonen.")

st.subheader("Ovulation")
st.write("Für ein genaueres Resultat, sollte der Test direkt am morgen, mit dem ersten Morgenurin gemacht werden.")
