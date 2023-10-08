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


st.header("Satellite Bytes: Unveiling Magnetic Secrets")
st.subheader("Spacecraft Data Analysis results")

# # Linki do nbviewer
# nbviewer_links = {
#     "ace_solution": "https://nbviewer.org/github/whosethere/spaceapp/blob/main/notebooks/ace_solution.ipynb",
#     "ace_wind_dscovr_solution": "https://nbviewer.org/github/whosethere/spaceapp/blob/main/notebooks/ace_wind_dscovr_solution.ipynb",
#     "dscovr_solution": "https://nbviewer.org/github/whosethere/spaceapp/blob/main/notebooks/dscovr_solution.ipynb",
#     "wind_solution": "https://nbviewer.org/github/whosethere/spaceapp/blob/main/notebooks/wind_solution.ipynb"
# }

# Linki do GitHub
github_links = {
    "ACE spacecraft data analysis": "https://github.com/whosethere/spaceapp/blob/main/notebooks/ace_solution.ipynb",

    "DSCOVR data analysis": "https://github.com/whosethere/spaceapp/blob/main/notebooks/dscovr_solution.ipynb",
    "WIND data analysis": "https://github.com/whosethere/spaceapp/blob/main/notebooks/wind_solution.ipynb",
    "Magnetic reconnection spacecrafts data": "https://github.com/whosethere/spaceapp/blob/main/notebooks/ace_wind_dscovr_solution.ipynb",
}

st.markdown("### GitHub Links:")
for name, link in github_links.items():
    st.markdown(f"[{name} notebook]({link})")

conclusion = """
## Dive into Space Data: Your Interactive Guide

I've created a public notebook for satellite data analysis. With Google Colab, anyone can now access and independently explore this intriguing dataset. Dive in and unravel the mysteries of cosmic measurements!

[Access the Notebook on Google Colab](https://colab.research.google.com/drive/1T9iH7yqZVzKfnaehDoB91DPK9fkHd2l7#scrollTo=aue4St2uwS9O)

"""


st.markdown(conclusion)

conclusion_1 = """
### Significance of Magnetic Field Direction
The \( Bz \) component of the magnetic field plays a pivotal role in the magnetic reconnection process. The dataset showcased significant periods where \( Bz \) was southward-oriented (negative values), indicating an enhanced likelihood for reconnection, especially when \( Bz \) values were below -1.7 nT.
"""

st.markdown(conclusion_1)


st.header("Data analysis conclusions")
conclusion_2 = """
### Solar Wind Speed's Influence on Reconnection
Higher solar wind speeds (above 376 km/s) can favor magnetic reconnection by driving more solar wind plasma into Earth's magnetosphere. The analysis revealed instances where the solar wind speed was notably high, correlating with a heightened probability of reconnection.
"""
st.markdown(conclusion_2)


conclusion_3 = """
### Proton Density as an Activity Indicator
Significant deviations in proton density, both above and below the mean, can be indicative of increased magnetospheric activity. The satellite data analysis pointed out periods where proton density substantially deviated from the average, suggesting enhanced interactions between the solar wind and Earth's magnetosphere.
"""

st.markdown(conclusion_3)

conclusion_4 = """
### Inter-Satellite Synergy: Unveiling Consistent Correlations in Space Data
After analyzing the data from all the satellites, it is evident that there is a significant correlation between them. The patterns observed across the datasets from ACE, WIND, and DSCOVR satellites consistently align, underscoring the interconnected nature of their measurements and the robustness of the findings.
"""

st.markdown(conclusion_4)

