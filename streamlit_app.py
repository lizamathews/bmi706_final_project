import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image

@st.cache
def load_data():

    # Read in the dataset
    cancer_df = pd.read_csv("data/all20states.txt", sep="\t")
    # Clean up
    # Some columns won't be used so we'll remove them: 
    cancer_df = cancer_df.drop(columns = ['Notes', 'State Code', 'Year Code', 'Age Group Code', 'Gender Code'])
    # All cancers listed in the 'Cause of death' column are malignant neoplasms - we can 
    # remove this identifier from the individual values
    causes = cancer_df['Cause of death'].tolist()
    causes = [i.split(' - ', 1)[0] for i in causes]
    cancer_df['Cause of death'] = causes

    return cancer_df

df = load_data()


# Title section
st.write("## BMI 706 Final Project")
st.write("#### Team Members: Liza Mathews, Renhao Luo, Sean Bai, Danny Jomaa")

# Load images
image_benign = "data/benign_tumor.png"
image_malig  = "data/malignant_tumor.png"

top_expander = st.expander("Overview of Benign and Malignant Neoplasms", expanded = True)
with top_expander:
    # A subheader in the expander
    st.subheader("Information about malignant neoplasms")
    # Create two columns so we can describe benign vs. malignant neoplasms
    col1,col2 = st.columns(2)
    benign = Image.open(image_benign)
    col1.caption("Benign")
    col1.image(benign, width = 15)
    col1.text("Description of benign neoplasms...")
    malig  = Image.open(image_malig)
    col2.caption("Malignant")
    col2.image(malig, width = 15)
    col2.text("Description of malignant neoplasms...")



