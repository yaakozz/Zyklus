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

medi2 = "medi2"
Mittag = [day[medi2]for key, day in file_medi1.items() if medi2 in day]

medi3 = "medi3"
Abend = [day[medi3]for key, day in file_medi1.items() if medi3 in day]

medi4 = "medi4"
Schlafen = [day[medi4]for key, day in file_medi1.items() if medi4 in day]

Tag = file_medi1.keys()

#taken_medi = dict((k, eval(k)) for k in ("Morgen", "Mittag", "Abend", "Schlafen", "Tag"))     #creating dictionary for panda dataframe
taken_medi = {
    "Morgen": Morgen,
    "Mittag": Mittag,
    "Abend": Abend,
    "Schlafen": Schlafen,
    "Tag": Tag
}
df = pd.DataFrame.from_dict(taken_medi, orient = "index", columns=['values'])
#st.dataframe(df, width=1024, height=768)
