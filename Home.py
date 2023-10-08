
import streamlit as st 
from constant import *
import numpy as np 
import pandas as pd
import io
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from graph_builder import *
from streamlit_player import st_player


st.set_page_config(page_title='Magnetic reconnection explained' ,layout="wide",page_icon='')# your CSS string)
# st.sidebar.markdown(info['Stackoverflow_flair'],unsafe_allow_html=True)
# st.subheader('Summary')
# st.write(info['Brief'])
# st.markdown('<style>{}</style>'.format(dark_theme_css), unsafe_allow_html=True)
# st.header('Magnetic Reconnection: Beauty, Power, and Disruption')
# st.write("Magnetic reconnection is a phenomenon where magnetic field lines intersect and rearrange themselves in space. This process is vital in astrophysics, playing a role in solar storms that can produce beautiful auroras on Earth. However, these storms can also disrupt satellites, navigation systems, and power grids. Thus, understanding magnetic reconnection helps us predict and mitigate the impact of solar storms on our technology.")
markdown_text = """
## Magnetic Reconnection: Beauty, Power, and Disruption

**Magnetic reconnection** is a phenomenon where **magnetic field lines** intersect and rearrange themselves in space. This process is vital in **astrophysics**, playing a role in **solar storms** that can produce beautiful **auroras** on Earth. However, these storms can also **disrupt satellites, navigation systems, and power grids**. Thus, understanding magnetic reconnection helps us **predict and mitigate** the impact of solar storms on our technology.
"""


st.markdown(markdown_text)
markdown_text = """
## Journey Through Time: Unraveling the Secrets of Magnetic Reconnection

Dive into the captivating history of magnetic reconnection, a cornerstone in understanding our universe. Explore our timeline to witness the milestones and discoveries that shaped modern astrophysics. Don't miss out on this cosmic journey!
"""
st.markdown(markdown_text)


st.subheader('Events Timeline📅')
# Sample custom CSS for streamlit-timeline in dark mode
# Custom CSS for dark theme styling of the identified classes


with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

def generate_link(tag):
    # W tym przypadku generujemy link do wyszukiwania Google dla danego tagu
    base_url = "https://www.google.com/search?q="
    return f"[{tag}]({base_url + tag})"

st.subheader('Concepts⚒️')


tags = [
    'IMF (Interplanetary Magnetic Field)',
    'Solar Wind',
    'Aurora Borealis',
    'Magnetosphere',
    'Magnetic Flux',
    'Solar Flares',
    'Coronal Mass Ejections (CMEs)',
    'Magnetic Shear',
    'Plasma Physics'
]


st.title("Interested? Explore these deeper topics.")


# Dla każdych trzech tagów, tworzymy nowy rząd z trzema kolumnami
for i in range(0, len(tags), 3):
    columns = st.columns(3)
    for j in range(3):
        if i + j < len(tags):  # Upewniamy się, że nie przekroczyliśmy listy tagów
            tag = tags[i + j]
            link = f"https://www.google.com/search?q={tag}"
            columns[j].markdown(f"""
            <div style="background-color: #1E1E1E; padding: 10px; border-radius: 5px; margin: 10px 0;">
                <a href="{link}" target="_blank" style="text-decoration: none; color: #FFF;">
                    🔗 {tag}
                </a>
            </div>
            """, unsafe_allow_html=True)

