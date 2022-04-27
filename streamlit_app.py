import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
from vega_datasets import data


##### 
# Load the data
#####
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

#####
# Header section
#####
st.markdown("<h1 style='text-align: center; color: black;'>Trends in Mortality due to Malignant Neoplasms: 2007-2016</h1>", unsafe_allow_html=True)
st.write("###### BMI 706 Final Project")
st.write("###### Team Members: Liza Mathews, Renhao Luo, Sean Bai, Danny Jomaa")

# Load images
image_benign = "data/benign_tumor.png"
image_malig  = "data/malignant_tumor.png"

top_expander = st.expander("Overview of Benign and Malignant Neoplasms", expanded = True)
with top_expander:
    # A subheader in the expander
    st.write("The visualizations below describe data on deaths due to malignant neoplasms in the United States. By understanding trends in deaths due to malignant neoplasms, we can identify diseases that we have been successful in treating and diseases that require further research. We have included a primer on benign and malignant neoplasms below to highlight the importance of studying trends in malignant neoplasms.")
    # Create two columns so we can describe benign vs. malignant neoplasms
    col1,col2 = st.columns(2)
    benign = Image.open(image_benign)
    col1.subheader("Benign")
    col1.image(benign, width = 300)
    col1.write("Benign neoplasms describe abnormal collections of cells that often grow slowly and do not spread. These tumors are typically well-formed, smooth, and have regular borders. Although they can become large, in which case it may be necessary to remove them, they do not invade surrounding tissue or spread to other parts of the body. These tumors are rarely life-threatening and can often be removed surgically without the need for further treatment.")
    malig  = Image.open(image_malig)
    col2.subheader("Malignant")
    col2.image(malig, width = 300)
    col2.write("Malignant neoplasms describe abnormal collections that grow quickly and have the potential to be life-threatening. Malignant tumors often have irregular shapes and borders because they invade surrounding tissue, making them challenging to remove surgically. Depending on the location of the tumor and the extent of growth and spread to other parts of the body, they can be treated with a combination of surgery, radiation, chemotherapy, biological agents, and more. The visualizations shown below use data on deaths due to malignant neoplasms.")

    st.write("The dataset used for this project was obtained from the CDC's Wide-ranging Online Data for Epidemiologic Research (WONDER) [project](https://wonder.cdc.gov/). The portal allows users to query a wide range of public health data published by the CDC for use in independent studies. The data shown below is specifically derived from the Compressed Mortality dataset, which includes mortality and population counts for all U.S. counties from 1968 to 2018. We queried this dataset for mortality rates due to malignant neoplasms between 2007 and 2016 in 20 different states.")
    st.write("Using the options below, you can filter the dataset for ______ to learn more about deaths due to particular neoplasms across the U.S.")


#####
# Options section
#####

# The year filter
#####
year_filter = st.slider(label = 'Year', 
                        min_value = df['Year'].min().item(), 
                        max_value = df['Year'].max().item(),
                        value = (2007,2009), step = 1,
                        help="Select the year range.")
# Subset the dataframe for the year of interest
subset = df[df["Year"].between(year_filter[0],year_filter[1])]


# The sex filter
#####
sex_filter = st.radio(label = 'Sex', options = ('All', 'Female', 'Male'), index = 0)
# Subset the dataframe for the sex of interest
if sex_filter == 'All':
    subset = subset
else:
    subset = subset[subset['Gender'] == sex_filter]


# The cancer filter
#####
cancer_default = 'Breast, unspecified'
cancer_filter = st.selectbox(label = 'Cancer', options = subset['Cause of death'].unique(),
                             index = np.where(subset['Cause of death'].unique() == cancer_default)[0][0].item(), 
                             help="Select the cancer type.")

# Subset the dataframe for the cancer of interest
subset = subset[subset['Cause of death'] == cancer_filter]



##### 
# Line chart section
#####

# Creating the data for the line chart
lc_dat = subset.groupby(['Year', 'Cause of death']).sum().reset_index()

chart = alt.Chart(lc_dat).mark_line().encode(
    x=alt.X("Year:N"),
    y=alt.Y("Deaths:Q")
    #color=alt.Color("Rate:Q", scale=alt.Scale(type='log', domain=(0.01,1000), clamp=True), title="Mortality #rate per 100k"),
    #tooltip=["Rate"],
).properties(
    title=f"Mortality rates for {cancer_filter} for {'all patients' if sex_filter == 'All' else ('males' if sex_filter == 'Male' else 'females')} between {year_filter[0]} and {year_filter[1]}",
)



### P2.5 ###

st.altair_chart(chart, use_container_width=True)


##### 
# Interactive Bar Graph Linked to Line chart section (4th task)
#####

totdeaths_state = subset.groupby("State").sum().reset_index()

bargraph = alt.Chart(totdeaths_state).mark_bar().encode(
    x="State:N",
    y="Deaths:Q",
).properties(
    title=f"Total Deaths for {cancer_filter} By State for {'all patients' if sex_filter == 'All' else ('males' if sex_filter == 'Male' else 'females')} between {year_filter[0]} and {year_filter[1]}",
)

rule = alt.Chart(totdeaths_state).mark_rule(color='orange').encode(
    y='mean(Deaths):Q'
)



st.altair_chart(bargraph + rule, use_container_width=True)



##### 
# US Map section
#####
width = 600
height  = 300
project = 'equirectangular'

states = alt.topo_feature(data.us_10m.url, 'states')
capitals = data.us_state_capitals.url

# background of US Maps
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    title='Map of US Cancer Rates',
    width=650,
    height=400
).project('albersUsa')


# Copied from Altair, we made not need capitals but state names for hover

# Points and text
hover = alt.selection(type='single', on='mouseover', nearest=True,
                      fields=['lat', 'lon'])

base = alt.Chart(capitals).encode(
    longitude='lon:Q',
    latitude='lat:Q',
)


background # <- this shows the greyed map


# Four further dev notes:

# Right now, only background for US map

# the bar graph can now show the subset data from the line graph with deaths total by state as well as a mean deaths line

# Can also consider changing it to death rate by state.. Need to link this to the US map, and that should be it for main tasks













# text = base.mark_text(dy=-5, align='right').encode(
#     alt.Text('city', type='nominal'),
#     opacity=alt.condition(~hover, alt.value(0), alt.value(1))
# )

# points = base.mark_point().encode(
#     color=alt.value('black'),
#     size=alt.condition(~hover, alt.value(30), alt.value(100))
# ).add_selection(hover)


