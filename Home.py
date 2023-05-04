# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:17:53 2023

@author: eevee
"""

import streamlit as st

# importing libraries --------------------------
import pandas as pd
import streamlit.components.v1 as components

#streamlit basic configurations
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Analysis of Disinformation Campaigns on Twitter*</p>'
st.markdown(title,unsafe_allow_html=True)

subh= '<p style = "font-family:Sans Serif; color:Grey; font-size: 20px;">Disinformation is false information that is knowingly shared with the intent to deceive.</p>'
st.markdown(subh,unsafe_allow_html=True)

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

# --------------------------------metrics ----------------------------------------------
title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 25px;">Quick Stats</p>'
st.markdown(title,unsafe_allow_html=True)

data = {'Total # Tweets':['112,350,112'],
        'Maximum # Likes':['257,454'],
        '% Tweets w/ Hashtag':['33%'],
        'Median # Followers':['3,084'],
        'Maximum # Followers':['2,883,076'],
        'Average # Days Account Active':['681']}

#stats = pd.DataFrame(data).set_index('Total # Tweets')

stats = pd.DataFrame(data)

#stats = pd.read_csv(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\Eevee's BIG DATA GRAPH CREATORS\STATS.xlsx")
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# style
th_props = [
  ('font-size', '20px'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', 'black'),
  ('background-color', '#c3fbcb')
  ]
                               
td_props = [
  ('font-size', '18px')
  ]
                                 
styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]

# table
df2=stats.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
st.table(df2)


#st.table(stats)


#---------------------------------MAP------------------------------------------

key= '<p style = "font-family:Sans Serif; font-weight:bold; color:#24547c; font-size: 22px;">Key insights:</p>'
st.markdown(key,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Serbia had the highest volume of tweets</p>'
st.markdown(i1,unsafe_allow_html=True)
i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• China had the most Twitter accounts</p>'
st.markdown(i2,unsafe_allow_html=True)

with open("TweetsPerCountryDeep2.html", 'r') as f:
        html_string = f.read()
components.v1.html(html_string, width=1000, height=400, scrolling=False)

# from PIL import Image

# tweetmap= Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\HopefullyOfficialGraphs\Tweets\TweetsMAP_DEEP_vert.png")
# acctmap = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\HopefullyOfficialGraphs\Accounts\AccountMAP_DEEP_vert.png")

# maptitle = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 30px;">Volume of Tweets Emerging from Countries</p>'
# st.markdown(maptitle,unsafe_allow_html=True)
# st.image(tweetmap)

c1, c2, c3 = st.columns(3)
with c1:
    st.write(" ")

with c2:
    note= '<p style = "font-family:Sans Serif; color:Black; font-size: 20px;">Gray = No tweets in dataset</p>'
    st.markdown(note,unsafe_allow_html=True)
with c3:
    st.write(" ")

# maptitle = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 30px;">Number of Twitter Accounts per Country</p>'
# st.markdown(maptitle,unsafe_allow_html=True)
# st.image(acctmap)

with open("AccountsPerCountryDEEP.html", 'r') as f:
        html_string = f.read()
components.v1.html(html_string, width=1000, height=400, scrolling=False)


c1, c2, c3 = st.columns(3)
with c1:
    st.write(" ")

with c2:
    note= '<p style = "font-family:Sans Serif; color:Black; font-size: 20px;">Gray = No tweets in dataset</p>'
    st.markdown(note,unsafe_allow_html=True)
with c3:
    st.write(" ")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

footnote= '<p style = "font-family:Sans Serif; color:Grey; font-size: 15px;">*Data from the Twitter Moderation Research Consortium</p>'
st.markdown(footnote,unsafe_allow_html=True)

