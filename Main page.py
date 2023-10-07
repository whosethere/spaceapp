
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


dark_theme_css = """
/* General Background and Text Color */
.tl-timeline, .tl-storyslider {
    background-color: #2c2c2c; /* Dark background color */
    color: #e0e0e0; /* Light text color */
}

/* Navigation Buttons */
.tl-slidenav-previous, .tl-slidenav-next {
    background-color: #3a3a3a; /* Slightly lighter than the general background for distinction */
    color: #f5f5f5; /* Lighter text color for better visibility */
}

.tl-slidenav-icon {
    background-color: #4a4a4a; /* Even slightly lighter shade for the icon's background */
}

/* Navigation Content Container */
.tl-slidenav-content-container {
    background-color: #3a3a3a;
    border: 1px solid #4a4a4a; /* Border to give some definition */
}

/* Titles and Descriptions inside Navigation */
.tl-slidenav-title, .tl-slidenav-description {
    color: #f5f5f5;
}

/* Slider Container */
.tl-slider-container-mask, .tl-slider-container {
    background-color: #2c2c2c;
}
"""

st.set_page_config(page_title='Magnetic reconnection explained' ,layout="wide",page_icon='')# your CSS string)
# st.sidebar.markdown(info['Stackoverflow_flair'],unsafe_allow_html=True)
# st.subheader('Summary')
# st.write(info['Brief'])
st.markdown('<style>{}</style>'.format(dark_theme_css), unsafe_allow_html=True)

st.subheader('Events Timeline📅')
# Sample custom CSS for streamlit-timeline in dark mode
# Custom CSS for dark theme styling of the identified classes








with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)


st.subheader('Concepts⚒️')
def phrases_tab():
    rows,cols = len(info['tags'])//skill_col_size,skill_col_size
    skills = iter(info['tags'])
    if len(info['tags'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break


with st.spinner(text=" Loading section..."):
    phrases_tab()
