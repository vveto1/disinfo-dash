# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 09:28:56 2023

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

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Time Analysis</p>'
st.markdown(title,unsafe_allow_html=True)


goal= '<p style = "font-family:Sans Serif; color:Grey; font-size: 20px;">Goal: Understand how trends in tweet volume over time reflect current events</p>'
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

#key= '<p style = "font-family:Sans Serif; font-weight:bold; color:#24547c; font-size: 22px;">Key insights:</p>'
#st.markdown(key,unsafe_allow_html=True)



from PIL import Image

@st.cache
def load_time_():
    timeline = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\HopefullyOfficialGraphs\Time\time.png")
    return timeline

@st.cache
def load_serbia():
    serbia = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\Plots_PNG\Time Series\Serbia_TS_PLot_M.png")
    return serbia 

@st.cache
def load_china():
    china = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\Plots_PNG\Time Series\China_TS_PLot.png")
    return china

@st.cache
def load_turkey():
    turkey = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\Plots_PNG\Time Series\Turkey_TS_PLot.png")
    return turkey

st.image(load_time_())

tdesc= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">The overall time series plot sees a steep drop in tweet volume late 2019. This does not mean that disinformation on Twitter dropped, but, rather, Twitter’s data collection dropped. While Twitter has no published information as to why this is the case, it is notable to review Twitter’s revenue. Between Q4 of 2019 and Q2 of 2020, Twitter’s revenue dropped from 1B to 683M which is roughly a 32% drop in revenue. This could have possibly affected the employee’s ability to perform this specific data collection. More recently, Twitter’s acquisition by Elon Musk led to an 80% reduction in staffing which has future implications on the state of collecting current disinformation data.</p>'
st.markdown(tdesc,unsafe_allow_html=True)
cite= '<p style = "font-family:Sans Serif; color:Grey; font-size: 13px;">Twitter. (July 22, 2022). Twitter revenue from 1st quarter 2011 to 2nd quarter 2022 (in million U.S. dollars) [Graph]. In Statista. Retrieved May 03, 2023, from https://www.statista.com/statistics/274568/quarterly-revenue-of-twitter/ </p>'
st.markdown(cite,unsafe_allow_html=True)



c1, c2 = st.columns((5,5))
with c1:
    st.image(load_serbia())
with c2:
    title = '<p style = "font-family:Sans Serif; color:Black; font-weight:bold; font-size: 22px;">Events in Serbia That Could Affect Tweet Volume</p>'
    st.markdown(title,unsafe_allow_html=True)
    
    yr = '<p style = "font-family:Sans Serif; color:Black; font-size: 18px;">Observations Related to Late 2018</p>'
    st.markdown(yr,unsafe_allow_html=True)
    i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• 6 April – The Trump administration imposes sanctions on seven Russian oligarchs and 17 senior government officials, accusing them of "malign activity around the globe." [1]</p>'
    st.markdown(i1,unsafe_allow_html=True)
    i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• A series of largely peaceful protests that lasted for over a year starting in late 2018. This was one of the longest running anti-government protests in Europe [4]</p>'
    st.markdown(i2,unsafe_allow_html=True)
    
c1, c2 = st.columns((5,5))
with c1:
    st.image(load_turkey())
with c2:
    title = '<p style = "font-family:Sans Serif; color:Black; font-weight:bold; font-size: 22px;">Events in Turkey That Could Affect Tweet Volume</p>'
    st.markdown(title,unsafe_allow_html=True)
    
    yr = '<p style = "font-family:Sans Serif; color:Black; font-size: 18px;">Observations Related to 2016</p>'
    st.markdown(yr,unsafe_allow_html=True)
    i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• 4 March – The Turkish government seized control of the "Zaman" journal, a large daily newspaper [6]</p>'
    st.markdown(i1,unsafe_allow_html=True)
    i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• 15 July – A failed military coup d etat attempt led to a state of emergency for 3 months [6] </p>'
    st.markdown(i2,unsafe_allow_html=True)
    i3= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• 24 August – Turkey has launched a cross border operation with Jarabulus under the code name "Operation Euphrates Shield" [6] </p>'
    st.markdown(i3,unsafe_allow_html=True)
    
    yr = '<p style = "font-family:Sans Serif; color:Black; font-size: 18px;">Observations Related to 2018</p>'
    st.markdown(yr,unsafe_allow_html=True)
    i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• 20 January - Operation Olive Branch started, a cross border military operation [5]</p>'
    st.markdown(i1,unsafe_allow_html=True)
    i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• 18 March - Afrin falls under the control of the Turk ish Armed Forces and the Syrian National Army [5] </p>'
    st.markdown(i2,unsafe_allow_html=True)
    i3= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• 9 July - After winning an absolute majority in the 2018 Turkish presidential election, Recep Tayyip Erdoğan took his oath during a ceremony attended by leaders of 22 countries [5] </p>'
    st.markdown(i3,unsafe_allow_html=True)


c1, c2 = st.columns((5,5))
with c1:
    st.image(load_china())
with c2:
    title = '<p style = "font-family:Sans Serif; color:Black; font-weight:bold; font-size: 22px;">Events in China That Could Affect Tweet Volume</p>'
    st.markdown(title,unsafe_allow_html=True)
    
    yr = '<p style = "font-family:Sans Serif; color:Black; font-size: 18px;">Observations Related to 2016</p>'
    st.markdown(yr,unsafe_allow_html=True)
    i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• In May of 2016 a Chinese environmentalist died due to an altercation with police in Beijing [2]</p>'
    st.markdown(i1,unsafe_allow_html=True)
    i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• The United States elected Donald Trump as president in 2016</p>'
    st.markdown(i2,unsafe_allow_html=True)
    i3= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• China has a larger push for satellite development and launching [2]</p>'
    st.markdown(i3,unsafe_allow_html=True)
    
    yr = '<p style = "font-family:Sans Serif; color:Black; font-size: 18px;">Observations Related to 2017</p>'
    st.markdown(yr,unsafe_allow_html=True)
    i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• Donald Trump visits China for the first time in November [3]</p>'
    st.markdown(i1,unsafe_allow_html=True)
    i2= '<p style = "font-family:Sans Serif; color:Grey; font-size: 18px;">• The United States directly attacks the Syrian government for the first time since the start of the Syrian civil war</p>'
    st.markdown(i2,unsafe_allow_html=True)
    
#-----------------works cited------------------
title = '<p style = "font-family:Sans Serif; color:Black; font-weight:bold; font-size: 20px;">Works Cited</p>'
st.markdown(title,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 13px;">1. Treasury designates Russian oligarchs, officials, and entities in response to worldwide malign activity. U.S. Department of the Treasury. (2018, November 6). Retrieved April 26, 2023, from https://home.treasury.gov/news/press-releases/sm0338 </p>'
st.markdown(i1,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 13px;">2. Wikimedia Foundation. (2022, July 11). 2016 in China. Wikipedia. Retrieved April 26, 2023, from https://en.wikipedia.org/wiki/2016_in_China</p>'
st.markdown(i1,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 13px;">3. Wikimedia Foundation. (2023, February 13). 2017 in China. Wikipedia. Retrieved April 26, 2023, from https://en.wikipedia.org/wiki/2017_in_China </p>'
st.markdown(i1,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 13px;">4. Wikimedia Foundation. (2023, January 29). 2018–2020 Serbian protests. Wikipedia. Retrieved April 26, 2023, from https://en.wikipedia.org/wiki/2018%E2%80%932020_Serbian_protests </p>'
st.markdown(i1,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 13px;">5. Wikimedia Foundation. (2023, March 10). 2018 in Turkey. Wikipedia. Retrieved April 26, 2023, from https://en.wikipedia.org/wiki/2018_in_Turkey </p>'
st.markdown(i1,unsafe_allow_html=True)

i1= '<p style = "font-family:Sans Serif; color:Grey; font-size: 13px;">6. Wikimedia Foundation. (2023, March 27). 2016 in Turkey. Wikipedia. Retrieved April 26, 2023, from https://en.wikipedia.org/wiki/2016_in_Turkey  </p>'
st.markdown(i1,unsafe_allow_html=True)
