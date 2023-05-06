# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:04:36 2023

@author: catar
"""

import streamlit as st
import pandas as pd
from jsonbin import load_data, save_data

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]

#Dataframe with pandas for medis

file_medi1=load_data(api_key, bin_id)

medi1 = "medi1"
Morgen = [day[medi1]for key, day in file_medi1.items() if medi1 in day]     #getting values from nested dictionary

Mittag = [day[medi1]for key, day in file_medi1.items() if medi1 in day]

Abend = [day[medi1]for key, day in file_medi1.items() if medi1 in day]

Schlafen = [day[medi1]for key, day in file_medi1.items() if medi1 in day]

Datum = file_medi1.keys()

taken_medi = dict((k, eval(k)) for k in ("Morgen", "Mittag", "Abend", "Schlafen", "Datum"))     #creating dictionary for panda dataframe
df = pd.DataFrame.from_dict(taken_medi, orient = "columns")

st.dataframe(df, width=1024, height=768)
