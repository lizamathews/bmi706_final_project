# BMI706 Final Project

Team members: Danny Jomaa, Liza Mathews, Renhao Luo, Sean Bai

Link to our proposal: https://docs.google.com/document/d/17xa9hFn81xM41hQRwzrBBKzNNgaszOYq1mJ7OzYgD3s/edit?usp=sharing

### Summarizing the Dataset

The dataset includes the following 10 attributes: State, State population, Year, Cause of death (full), Cause of death (ICD-10 code), Number of deaths, Sex, Age group, Race, and Hispanic Origin. To avoid any issues with storage, we will subset the overall dataset for the time period, 2007-2016 (a 9-year time period). Geographic data will be included from the following 20 states: Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, and Maine. Our visualization will report data about deaths caused by malignant neoplasms, grouped into: Malignant neoplasms of lip, oral cavity and pharynx; malignant neoplasms of digestive organs; malignant neoplasms of respiratory and intrathoracic organs; malignant neoplasms of bone and articular cartilage; melanoma and other malignant neoplasms of skin; malignant neoplasms of mesothelial and soft tissue; malignant neoplasm of breast; malignant neoplasms of female genital organs; malignant neoplasms of male genital organs; malignant neoplasms of urinary tract; malignant neoplasms of eye, brain and other parts of central nervous system; malignant neoplasms of thyroid and other endocrine glands; and malignant neoplasms of lymphoid, haematopoietic and related tissue. ICD-10 codes will also be reported for each grouping. Years will be reported in 1-year increments. Sex will be reported as male or female. Ages will be reported in 5-year intervals between the ages of 1 and 84, with additional categories for < 1 year old and 84+ years old. Overall, there are 28,413 rows of our dataframe, with each row containing information on the number of deaths attributed to a particular cancer in a given state, year, age group, and sex.

### Dataset Description
The CDC WONDER online database offers a rich ad-hoc query system for analyzing public health data. Within this database, we will be using the Compressed Mortality dataset, which includes mortality and population counts for all U.S. counties for the years 1968 to 2018. 

### Exploratory Visualization
For this project, we will query the data regarding the malignant neoplasm from the CDC-WONDER: Mortality website, and prepare a web dashboard for the users to interact with the data and extract useful information for different purposes. Based on the queried data described in the Dataset Summary section above, we could answer various questions regarding the dataset. Some of the questions are listed here: 
How does the number of deaths due to malignant neoplasm change over the years?
Are males or females affected the most by the malignant neoplasm?
Which state has the highest/lowest number of deaths in a given year? 
What is the doctor’s diagnosis or ICD code of the cause of death? 

