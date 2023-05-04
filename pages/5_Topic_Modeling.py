# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:15:47 2023

@author: Administrator
"""

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

#streamlit basic configurations
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Topic Modeling</p>'
st.markdown(title,unsafe_allow_html=True)


goal= '<p style = "font-family:Sans Serif; color:Grey; font-size: 20px;">Goal: Identify what key words/topics are frequently used in the tweets</p>'
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

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Disinformation spread from accounts originating in Venezuela had a distinct focus on political events in the United States with words such as “Trump”, “Obama”, “inauguration”, “white_house”, “immigration”, “ban”, and “sancutary_cities”. </p>'
st.markdown(i1,unsafe_allow_html=True)

i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• The most common term for disinformative Russian tweets was “Trump” followed by indicators of links being shared such as “https”, “amp”, and “video”. </p>'
st.markdown(i2,unsafe_allow_html=True)

i3= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Most of China’s topics were tightly clustered together with Twitter buzzwords such as “follow”, “retweet”, and “like” being the most common terms. </p>'
st.markdown(i3,unsafe_allow_html=True)


from streamlit import components

d= '<p style = "font-family:Sans Serif; font-weight:bold; color:#24547c; font-size: 22px;">Select a country:</p>'
st.markdown(d,unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    country = st.selectbox('Topic Modeling Results for...',['Russia','China','Venezuela'])
with c2:
    st.write(' ')
with c3:
    st.write(' ')
#rus = st.checkbox("Russia Results")
if country=='Russia':
    st.header('Topic Modeling Results: Russia')
    with open("C:/Users/eevee/Cal Poly/Vanessa Christine Veto - Redo Twitter Data/LDA/Russia/rus_lda.html", 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1200, height=800, scrolling=True)

#china = st.checkbox("China Results")
if country=='China':
    st.header('Topic Modeling Results: China')
    with open("C:/Users/eevee/Cal Poly/Vanessa Christine Veto - Redo Twitter Data/LDA/China/china_lda.html", 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1200, height=800, scrolling=True)

#ven = st.checkbox("Venezuela Results", value=True)
if country=='Venezuela':
    st.header('Topic Modeling Results: Venezuela')
    with open("C:/Users/eevee/Cal Poly/Vanessa Christine Veto - Redo Twitter Data/LDA/Venezuela/ven_lda.html", 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1200, height=800)