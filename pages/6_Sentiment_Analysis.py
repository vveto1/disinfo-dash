# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:50:00 2023

@author: eevee
"""

# importing libraries --------------------------
import streamlit as st
import pandas as pd


#streamlit basic configurations
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Sentiment Analysis</p>'
st.markdown(title,unsafe_allow_html=True)

goal= '<p style = "font-family:Sans Serif; color:Grey; font-size: 20px;">Goal: Understand the sentiment being expressed in tweets</p>'
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

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Polarity is a continuous numerical value ranging from -1 to 1, where -1 represents the most negative sentiment and 1 represents the most positive sentiment. The score is interpreted as the degree of sentiment intensity, with higher absolute values indicating stronger sentiments.</p>'
st.markdown(i1,unsafe_allow_html=True)

i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">    ◦ An overall polarity of [-1,0) corresponds to a negative sentiment</p>'
st.markdown(i2,unsafe_allow_html=True)

i3= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">    ◦ An overall polarity of 0 corresponds to a neutral sentiment</p>'
st.markdown(i3,unsafe_allow_html=True)

i4= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">    ◦ An overall polarity of (0,1] corresponds to a positive sentiment</p>'
st.markdown(i4,unsafe_allow_html=True)

i5= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Overall, a larger segment of the tweets are associated as having positive sentiment (41.6%) compared to negative sentiment (25.2%)</p>'
st.markdown(i5,unsafe_allow_html=True)

i6= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Positive sentiment tweets have higher interactions compared to negative sentiment</p>'
st.markdown(i6,unsafe_allow_html=True)

i7= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">    ◦ More extreme sentiment did not receive as much interaction for both positive and negative classifications</p>'
st.markdown(i7,unsafe_allow_html=True)

i8= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• A steady decline in average polarity overall since 2010 and a slight increase in 2019</p>'
st.markdown(i8,unsafe_allow_html=True)

i9= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">    ◦ This is due to an increase in negative polarity and a slight decrease in positive polarity</p>'
st.markdown(i9,unsafe_allow_html=True)

i10= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Of the top countries within our data set, Russia and Venezuela have maintained a lower sentiment than the average of all countries</p>'
st.markdown(i10,unsafe_allow_html=True)

i11= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">    ◦ Since 2020, China and Russia have a far lower polarity score compared to the overall average in that time span</p>'
st.markdown(i11,unsafe_allow_html=True)
#○


from PIL import Image

@st.cache
def load_pie():
    pie = Image.open(r"weetsBySent.png")
    return pie
@st.cache
def load_countries():
    countries = Image.open(r"AvgPolCountry.png")
    return countries
@st.cache
def load_neginter():
    neginter = Image.open(r"Neginter.png")
    return neginter
@st.cache
def load_posinter():
    posinter = Image.open(r"Posinter.png")
    return posinter
@st.cache
def load_avgnegyr():
    avgnegyr = Image.open(r"Avgnegyear.png")
    return avgnegyr
@st.cache
def load_avgposyr():
    avgposyr = Image.open(r"Avgposyear.png")
    return avgposyr
@st.cache
def load_avgyr():
    avgyr = Image.open(r"Avgyear.png")
    return avgyr
@st.cache
def load_yearmeanpol():
    yearmeanpol = Image.open(r"yearmeanpol.png")
    return yearmeanpol



c1, c2 = st.columns((3,5))

with c1:
    st.image(load_pie())
with c2:
    st.image(load_countries())

c3, c4 = st.columns(2)

with c3:
    st.image(load_neginter())
with c4:
    st.image(load_posinter())

c5, c6 = st.columns(2)

with c5: 
    st.image(load_avgnegyr())
with c6:
    st.image(load_avgposyr())

c7, c8 = st.columns(2)

with c7:
    st.image(load_avgyr())
with c8:
    st.image(load_yearmeanpol())
