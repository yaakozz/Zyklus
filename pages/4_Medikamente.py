# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:04:36 2023

@author: catar
"""

import streamlit as st
import pandas as pd
import json

#Dataframe with pandas for medis
with open("data.json", "r")as file: 
    file_medi1 = json.load(file)

medi1 = "medi1"
medi1s = [day[medi1]for key, day in file_medi1.items() if medi1 in day]

def medi1_element(medi1s):
    taken_medi1s = []
    for a in medi1s:
        if a != "Paracetamol" or "Ibuprofen" or "Acetylsalicylsäure" or "Naproxen" or "Diclofenac":
            taken_medi1s.append(a)
    return taken_medi1s

taken_medi1ss = medi1_element(medi1s)

drf = pd.DataFrame({
    "medi1" : taken_medi1ss,
    "day" : file_medi1.keys()})

st.write("Eingenommene Medikamente", taken_medi1ss)