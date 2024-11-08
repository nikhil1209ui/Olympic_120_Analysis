# Olympics Data Analysis and Visualization

## Overview
This project provides an exploratory data analysis (EDA) and visual insights into the Olympics dataset. Using Python, Jupyter Notebook, and Streamlit, the project analyzes patterns, medal tallies, country-specific performance, and athlete statistics. The primary goal is to allow users to explore historical Olympic data in an interactive web app.

---
Datasets
-

athlete_events.csv: Contains information about athletes, including names, countries, events, and medal records.

noc_regions.csv: Maps National Olympic Committees (NOC) codes to respective regions/countries.

---
Project Structure
-
EDA: Conducted in Jupyter Notebook to clean and analyze the dataset.

Streamlit App: Interactive app for visualizing the data.

Helper and Preprocessor Scripts: Scripts used to process and structure data for the Streamlit app.

---
Key Files
-
EDA.ipynb: Contains data cleaning, analysis, and visualizations.

app.py: Streamlit app for interactive data exploration.

preprocessor.py: Preprocessing functions for data merging and transformation.

helper.py: Contains functions for querying and aggregating data for app visualization.

---
Installation
-
Clone this repository and navigate to the project directory.
Install required dependencies:

`pip install -r requirements.txt`

Ensure that athlete_events.csv and noc_regions.csv are in the project directory.

---
Running the Application
-

1. Jupyter Notebook:
   
   Open .ipynb to view the exploratory analysis.
   
2. Streamlit App:
 
   Run the app:
   `streamlit run app.py`

---
Analysis in EDA.ipynb
-
- Data Cleaning:

. Filtered data for only "Summer" Olympics.

. Removed duplicates and merged athlete data with regional codes.

- Medal Tally Calculation:

. Aggregated medal counts by country for each year.

- Visualizations:

. Line charts for participation trends over time.

. Heatmaps for events per sport over the years.

. Distribution plots for athlete ages by medal type.

- Functions:

. fetch_year_country(): Fetches medal tally for a specific year and/or country.
. most_successful(): Identifies top medalists in each sport.

---
Streamlit Application (app.py)
-
. Sidebar Options:-

1. Medal Tally: View medal counts by year and country.

2. Overall Analysis: Summary statistics including total editions, sports, athletes, and a timeline of events and participants.

3. Country-wise Analysis: Examine medal tallies and top athletes for selected countries.

4. Athlete-wise Analysis: Analyze age distributions and gender participation trends.

. Key Features

1. Interactive Graphs: Includes line plots and heatmaps using Plotly and Seaborn.
2. Data Selection: Filters by year, country, and sport.

---
helper.py Functions
-
1. fetch_year_country(): Retrieves medal data based on year and country.
 
2. medal_tally(): Aggregates medal counts.
 
3. country_year_list(): Generates lists of unique years and countries for selection.

---
preprocessor.py
-
preprocess(): Merges athlete_events and noc_regions datasets and handles data preprocessing for analysis.

---
Technologies Used
-
Python: Core language for data manipulation and app development.

Pandas, NumPy: Data handling and preprocessing.

Plotly, Seaborn, Matplotlib: Data visualization.

Streamlit: Web app framework.
