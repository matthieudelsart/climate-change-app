import streamlit as st

st.set_page_config(
    page_title="Vizualizing Climate Change",
    page_icon="🌍",
)

st.write("# Welcome to our climate change visualization app! 🌍📈")

st.sidebar.success("Select the data to be displayed above.")

st.markdown(
    """
    This page leverages the GISTEMP dataset to visualize global temperature anomalies over time. \n
    The original data can be found [here](https://data.giss.nasa.gov/gistemp/). 
"""
)
