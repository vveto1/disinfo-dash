# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:52:33 2023

@author: eevee
"""

# importing libraries --------------------------
import streamlit as st
import pandas as pd


#streamlit basic configurations
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Language Analysis</p>'
st.markdown(title,unsafe_allow_html=True)

goal= '<p style = "font-family:Sans Serif; color:Grey; font-size: 20px;">Goal: Understand what countries/communities disinformation spreaders are targeting by analyzing the distribution of languages used in disinformative tweets</p>'
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

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Turkish is the most commonly used language, followed by Serbian and Spanish.</p>'
st.markdown(i1,unsafe_allow_html=True)

i5= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• China most commonly sent disinformative tweets in English, and Iran sent disinformative tweets in English nearly as much as in Arabic.</p>'
st.markdown(i5,unsafe_allow_html=True)

i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• For all countries analyzed besides China, the most common language used was the native language, implying internal attacks</p>'
st.markdown(i2,unsafe_allow_html=True)

i3= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• For these countries, the second most common language was English, implying external attacks to the United States and other english-speaking communities</p>'
st.markdown(i3,unsafe_allow_html=True)

i4= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Serbia, Russia, and Venezuela’s third most commonly used languages are languages of nearby countries- Slovenia (Slovenian) for Serbia, Ukraine (Ukrainian) for Russia, and Brazil (Portuguese) for Venezuela. </p>'
st.markdown(i4,unsafe_allow_html=True)

from PIL import Image

@st.cache
def load_overall():
    overall = Image.open(r"langBar.png")
    return overall
@st.cache
def load_china():
    china = Image.open(r"chinaLang.png")
    return china
@st.cache
def load_iran():
    iran = Image.open(r"iranLang.png")
    return iran
@st.cache
def load_russia():
    russia = Image.open(r"russiaLang.png")
    return russia
@st.cache
def load_serbia():
    serbia = Image.open(r"serbLang.png")
    return serbia
@st.cache
def load_turkey():
    turkey = Image.open(r"turkLang.png")
    return turkey
@st.cache
def load_ven():
    ven = Image.open(r"venLang.jpg")
    return ven

l, m, r = st.columns((1,10,1))

with l:
    st.text(' ')
with m:
    st.image(load_overall(), width =750)
with r:
    st.text(' ')
    
st.text(' ')
st.text(' ')
key= '<p style = "font-family:Sans Serif; font-weight:bold; color:#24547c; font-size: 35px;">Language Breakdown for Top Countries</p>'
st.markdown(key,unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.image(load_china())
with c2:
    st.image(load_iran())

    
c3, c4 = st.columns(2)
with c3:
    st.image(load_russia())
with c4:
    st.image(load_serbia())

c5, c6 = st.columns(2)
with c5:
    st.image(load_turkey())
with c6:
    st.image(load_ven())
