# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:49:26 2023

@author: eevee
"""

# importing libraries --------------------------
import streamlit as st
import pandas as pd


#streamlit basic configurations
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Engagement Analysis</p>'
st.markdown(title,unsafe_allow_html=True)

goal= '<p style = "font-family:Sans Serif; color:Grey; font-size: 20px;">Goal: Understand what level of engagement disinformative tweets are receiving and how the difference between countries highlights differences strategies for spreading disinformation</p>'
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


i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Tweets generally got very low engagement</p>'
st.markdown(i1,unsafe_allow_html=True)

i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Tweets from Thailand, Spain, and Mexico received a far higher interaction/follower ratio than any other country, for all forms of interaction.</p>'
st.markdown(i2,unsafe_allow_html=True)

i5= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Countries that spam large amounts of tweets are receiving less engagement for those tweets, while countries that are sending out less tweets are receiving higher engagement.</p>'
st.markdown(i5,unsafe_allow_html=True)


from PIL import Image

@st.cache
def load_overall():
    overall = Image.open(r"OverallInteraction.png")
    return overall
@st.cache
def load_likes():
    likes = Image.open(r"L.jpg")
    return likes
@st.cache
def load_rt():
    rt = Image.open(r"RT.jpg")
    return rt
@st.cache
def load_rep():
    rep = Image.open(r"RepliesGraph.jpg")
    return rep

l, m, r = st.columns((1,10,1))

with l:
    st.text(' ')
with m:
    st.image(load_overall(), width =750)
with r:
    st.text(' ')

#st.image(overall)

c1, c2 = st.columns(2)

with c1:
    st.image(load_likes())
    st.image(load_rt())
with c2:
    st.image(load_rep())

