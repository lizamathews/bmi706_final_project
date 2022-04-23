import altair as alt
import pandas as pd
import streamlit as st
import numpy as np

@st.cache
def load_data():

    cancer_df = pd.read_csv("data/all20states.txt", sep="\t")

    return cancer_df

df = load_data()





st.write("## BMI 706 Final Project")
st.write("### Team Members:")


