import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import reportfunctions as rf

st.set_page_config(page_title="Aniss Football Report", layout="wide",initial_sidebar_state="expanded")
# Select Player
a = st.sidebar.selectbox("League",("",1,2,3,4))
c= ""
if a != "":
    b = st.sidebar.selectbox("Club",("",1,2,3,4)) 
    if b != "":
        c = st.sidebar.selectbox("Player",("",1,2,3,4)) 

col1,col2 = st.columns([1,3],gap="small")

with col1:
    if c!="":
        #if player.position =="GK": rf.goalkeeper_rep(c)
        #else: rf.outfield_rep(c)
        with st.container(height=500):
            with st.container(height=150,border=False):
                pass
            st.write(c)

with col2:
    st.write("A")

