# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:50:50 2023

@author: eevee
"""

# importing libraries --------------------------
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#streamlit basic configurations
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Account Analysis</p>'
st.markdown(title,unsafe_allow_html=True)

goal= '<p style = "font-family:Sans Serif; color:Grey; font-size: 20px;">Goal: Understand what level of following disinformation spreaders have on Twitter</p>'
st.markdown(goal,unsafe_allow_html=True)


st.sidebar.markdown('''
---
Created by Eevee Murdock, Ethan Eichten, Jack Reed, and Vanessa Veto
''')

st.sidebar.markdown('''
Sponsor: Dr. Puneet Agarwal
''')

st.sidebar.markdown('''
Advisor: Dr. Tali Freed
''')

st.sidebar.markdown('''
---
California Polytechnic State University, San Luis Obispo
''')


key= '<p style = "font-family:Sans Serif; font-weight:bold; color:#24547c; font-size: 22px;">Key insights:</p>'
st.markdown(key,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• The majority of the accounts in the dataset had less than 10 followers.</p>'
st.markdown(i1,unsafe_allow_html=True)

i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Qatar had the highest number of average followers/account, followed by  Russia and Egypt</p>'
st.markdown(i2,unsafe_allow_html=True)


from PIL import Image
@st.cache
def load_follcountry():
    follcountry = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\HopefullyOfficialGraphs\Accounts\followersByCountry.png")
    return follcountry
@st.cache
def load_foll():
    foll = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\HopefullyOfficialGraphs\Accounts\followers-bar.png")
    return foll
#follint = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\HopefullyOfficialGraphs\Accounts\followersVsInteraction.png")

st.image(load_follcountry())

l, m, r = st.columns((1,10,1))

with l:
    st.text(' ')
with m:
    st.image(load_foll(), width =750)
with r:
    st.text(' ')
#st.image(foll)
#st.image(follint)