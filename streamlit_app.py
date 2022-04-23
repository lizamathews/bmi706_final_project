import altair as alt
import pandas as pd
import streamlit as st

@st.cache
def load_data():

    cancer_df = pd.read_csv("data/all20states.txt", sep="\t")

    return cancer_df

df = load_data()
