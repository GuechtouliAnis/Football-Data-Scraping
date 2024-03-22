import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import Position_dr as pdr

st.set_page_config(page_title="Blue Lock", layout="wide")
conn = sqlite3.connect('Blue Lock.db')
cur = conn.cursor()
cur.execute('SELECT * FROM Positions')
rows = cur.fetchall()
conn.close()
positions = ["Player", "GK", "RB", "CB", "LB", "DM", "RM", "CM", "LM", "AM", "RW", "SS", "LW", "ST"]
df = pd.DataFrame(rows, columns=positions)

col1, col2 = st.columns([1, 1])

with col1:
    selected = st.selectbox("Player", options=df['Player'].tolist())
    pdr.positions(df[df["Player"]==selected])

for p in positions[1:]:
    s = ""
    st.write(p)
    for el in list(df[df[p]==1]['Player']):
        s += el +" - "
    st.write(s[:-2])