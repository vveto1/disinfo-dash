# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:49:44 2023

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

title = '<p style = "font-family:Roboto,Sans-Serif; font-weight:bold; color:#24547c; font-size: 40px;">Data Size</p>'
st.markdown(title,unsafe_allow_html=True)



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

from PIL import Image

info = Image.open(r"C:\Users\eevee\Cal Poly\Vanessa Christine Veto - Redo Twitter Data\DATASIZE.png")
st.image(info)