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
Olympics120analysis.ipynb: Contains data cleaning, analysis, and visualizations.

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

 <img width="371" alt="image" src="https://github.com/user-attachments/assets/14ee4a3c-0825-4bc8-b894-8bc902533cdf">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/221f2e23-838d-49ad-ba10-28fd2a988435">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/87d08a61-46fd-455e-be58-f517b6db1d8c">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/0466d0f8-795b-4af0-94e8-23b54e6f6347">

---

2. Overall Analysis: Summary statistics including total editions, sports, athletes, and a timeline of events and participants.

 <img width="371" alt="image" src="https://github.com/user-attachments/assets/392c114d-6ec3-4f31-8144-07d82f1ea71b">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/f2d9d55d-3691-45f5-9367-5753d4079d33">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/a2ac8b04-f2ac-4ff9-b7f4-c7a0432d4005">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/389c25e1-6876-4dd0-b4f5-e283a706b570">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/9d5f4edb-7319-4048-a609-345967431d8d">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/ac5bec98-3e59-459a-966a-702bafb28a4a">
 <img width="365" alt="image" src="https://github.com/user-attachments/assets/cb650688-c158-408f-83a2-f37d821d79d9">
 <img width="371" alt="image" src="https://github.com/user-attachments/assets/3809579e-b57b-45c4-8f07-8aca9547a758">

---

3. Country-wise Analysis: Examine medal tallies and top athletes for selected countries.

 <img width="371" alt="image" src="https://github.com/user-attachments/assets/021961a1-434b-4628-a0e2-0f2b290cd3b1">
 <img width="385" alt="image" src="https://github.com/user-attachments/assets/a32db3eb-8dc3-4970-ad80-d50249823e9b">
 <img width="359" alt="image" src="https://github.com/user-attachments/assets/1370d59d-1f93-418e-b125-4a9621609207">
 <img width="364" alt="image" src="https://github.com/user-attachments/assets/ee7f3bc3-6062-42c1-a425-f437a3620966">

---

4. Athlete-wise Analysis: Analyze age distributions and gender participation trends.

   <img width="400" alt="image" src="https://github.com/user-attachments/assets/3cf057d9-7449-4446-9f4d-d5a5b0a0e5f2">
   <img width="386" alt="image" src="https://github.com/user-attachments/assets/6da40872-29e5-4c20-93c3-f299d0f0105d">
   <img width="302" alt="image" src="https://github.com/user-attachments/assets/7bb34615-244b-43aa-97b0-12a98bdf74a5">
   <img width="281" alt="image" src="https://github.com/user-attachments/assets/f2e66b98-a029-4725-8846-01e68d912d03">
   <img width="282" alt="image" src="https://github.com/user-attachments/assets/d174ab33-ead7-4751-ab38-24b4da69d569">


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
