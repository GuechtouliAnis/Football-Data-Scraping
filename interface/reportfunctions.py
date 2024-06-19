import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sqlite3

# To make
def connect_files(repo):
    pass

def positions (player):

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
    if int(player['GK'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((0.3, 12.5), 15.7, 39, edgecolor='orange', facecolor='orange'))  # GK
    if int(player['RB'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((0.3, 0.2), 32.5, 11.4, edgecolor='cyan', facecolor=(0, 1, 1, 1)))  # RB
    if int(player['CB'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((17.1, 12.4), 15.7, 39.3, edgecolor='cyan', facecolor=(0, 1, 1, 1)))  # CB
    if int(player['LB'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((0.3, 52.5), 32.5, 11.4, edgecolor='cyan', facecolor=(0, 1, 1, 1)))  # LB

    if int(player['DM'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((33.3, 12.4), 11, 39.3, edgecolor='green', facecolor=(0, 1, 0, 1)))  # DM
    if int(player['RM'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((33.3, 0.2), 38.5, 11.4, edgecolor='green', facecolor=(0, 1, 0, 1)))  # RM
    if int(player['CM'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((44.9, 12.4), 13, 39.3, edgecolor='green', facecolor=(0, 1, 0, 1)))  # CM
    if int(player['LM'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((33.3, 52.5), 38.5, 11.4, edgecolor='green', facecolor=(0, 1, 0, 1)))  # LM
    if int(player['AM'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((58.5, 12.4), 13.3, 39.3, edgecolor='green', facecolor=(0, 1, 0, 1)))  # AM

    if int(player['RW'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((72.4, 0.2), 27.2, 11.4, edgecolor='red', facecolor=(1, 0, 0, 1)))  # RW
    if int(player['SS'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((72.4, 12.4), 13, 39.3, edgecolor='red', facecolor=(1, 0, 0, 1)))  # SS
    if int(player['LW'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((72.4, 52.5), 27.2, 11.4, edgecolor='red', facecolor=(1, 0, 0, 1)))  # LW

    if int(player['ST'].iloc[0] == 1):
        ax.add_patch(patches.Rectangle((86, 12.4), 13.6, 39.3, edgecolor='red', facecolor=(1, 0, 0, 1)))  # ST

    circle = patches.Circle((50, 32), radius=9.15, edgecolor='black', facecolor='none')
    ax.add_patch(circle)

    ax.set_ylim([0, 64])
    ax.set_xlim([0, 100])
    # Set figure background color to grey
    fig.patch.set_facecolor('grey')
    ax.axis('off')
    st.pyplot(fig)

def powers(player):
    pass

def goalkeeper_rep(player):
    pass

def outfield_rep(player):
    pass



