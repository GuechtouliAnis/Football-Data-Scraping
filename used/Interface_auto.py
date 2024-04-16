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
fig, ax = plt.subplots(figsize=(10, 5))

# Drawing the field
ax.plot([0, 16.5], [12, 12], color='black')
ax.plot([0, 16.5], [52, 52], color='black')
ax.plot([16.5, 16.5], [12, 52], color='black')
ax.plot([0, 5.5], [23, 23], color='black')
ax.plot([0, 5.5], [41, 41], color='black')
ax.plot([5.5, 5.5], [41, 23], color='black')
ax.plot([0.1, 0.1], [41, 23], color='green')

ax.plot([83.5, 100], [12, 12], color='black')
ax.plot([83.5, 100], [52, 52], color='black')
ax.plot([83.5, 83.5], [12, 52], color='black')
ax.plot([94.5, 100], [23, 23], color='black')
ax.plot([94.5, 100], [41, 41], color='black')
ax.plot([94.5, 94.5], [41, 23], color='black')
ax.plot([99.9, 99.9], [41, 23], color='green')

# center
ax.plot([50, 50], [0, 64], color='black')
ax.plot([0, 100], [0, 0], color='black')
ax.plot([0, 100], [64, 64], color='black')
ax.plot([0, 0], [0, 64], color='black')
ax.plot([100, 100], [0, 64], color='black')

# Splitting
ax.add_patch(patches.Rectangle((0.3, 12.5), 15.7, 39, edgecolor='orange', facecolor='orange'))  # GK
ax.add_patch(patches.Rectangle((0.3, 0.2), 32.5, 11.4, edgecolor='cyan', facecolor='cyan'))  # RB
ax.add_patch(patches.Rectangle((17.1, 12.4), 15.7, 39.3, edgecolor='cyan', facecolor='cyan'))  # CB
ax.add_patch(patches.Rectangle((0.3, 52.5), 32.5, 11.4, edgecolor='cyan', facecolor='cyan'))  # LB

ax.add_patch(patches.Rectangle((33.3, 12.4), 11, 39.3, edgecolor='green', facecolor='green'))  # DM
ax.add_patch(patches.Rectangle((33.3, 0.2), 38.5, 11.4, edgecolor='green', facecolor='green'))  # RM
ax.add_patch(patches.Rectangle((44.9, 12.4), 13, 39.3, edgecolor='green', facecolor='green'))  # CM
ax.add_patch(patches.Rectangle((33.3, 52.5), 38.5, 11.4, edgecolor='green', facecolor='green'))  # LM
ax.add_patch(patches.Rectangle((58.5, 12.4), 13.3, 39.3, edgecolor='green', facecolor='green'))  # AM

ax.add_patch(patches.Rectangle((72.4, 0.2), 27.2, 11.4, edgecolor='red', facecolor='red'))  # RW
ax.add_patch(patches.Rectangle((72.4, 12.4), 13, 39.3, edgecolor='red', facecolor='red'))  # SS
ax.add_patch(patches.Rectangle((72.4, 52.5), 27.2, 11.4, edgecolor='red', facecolor='red'))  # LW

ax.add_patch(patches.Rectangle((86, 12.4), 13.6, 39.3, edgecolor='red', facecolor='red'))  # SS
""
circle = patches.Circle((50, 32), radius=9.15, edgecolor='black', facecolor='none')
ax.add_patch(circle)

ax.set_ylim([0, 64])
ax.set_xlim([0, 100])

ax.axis('off')  # Hiding x and y axes

with col2:
    st.pyplot(fig)
with col1:
    selected=st.selectbox("",df['Player'])
    pdr.positions(df[df["Player"]==selected])