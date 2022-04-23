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
    st.text("The visualizations below describe data on deaths due to malignant neoplasms in the United States. By understanding trends in deaths due to malignant neoplasms, we can identify diseases that we have been successful in treating and diseases that require further research. We have included a primer on benign and malignant neoplasms below to highlight the importance of studying trends in malignant neoplasms.")
    # Create two columns so we can describe benign vs. malignant neoplasms
    col1,col2 = st.columns(2)
    benign = Image.open(image_benign)
    col1.caption("Benign")
    col1.image(benign, width = 100)
    col1.text("Benign neoplasms describe abnormal collections of cells that often grow slowly and do not spread. These tumors are typically well-formed, smooth, and have regular borders. Although they can become large, in which case it may be necessary to remove them, they do not invade surrounding tissue or spread to other parts of the body. These tumors are rarely life-threatening and can often be removed surgically without the need for further treatment.")
    malig  = Image.open(image_malig)
    col2.caption("Malignant")
    col2.image(malig, width = 100)
    col2.text("Malignant neoplasms describe abnormal collections that grow quickly and have the potential to be life-threatening. Malignant tumors often have irregular shapes and borders because they invade surrounding tissue, making them challenging to remove surgically. Depending on the location of the tumor and the extent of growth and spread to other parts of the body, they can be treated with a combination of surgery, radiation, chemotherapy, biological agents, and more. The visualizations shown below use data on deaths due to malignant neoplasms.")

    st.text("The dataset used for this project was obtained from the CDC's Wide-ranging Online Data for Epidemiologic Research (WONDER) [project](https://wonder.cdc.gov/). The portal allows users to query a wide range of public health data published by the CDC for use in independent studies. The data shown below is specifically derived from the Compressed Mortality dataset, which includes mortality and population counts for all U.S. counties from 1968 to 2018. We queried this dataset for mortality rates due to malignant neoplasms between 2007 and 2016 in 20 different states.")
    st.text("Using the options below, you can filter the dataset for ______ to learn more about deaths due to particular neoplasms across the U.S.")



