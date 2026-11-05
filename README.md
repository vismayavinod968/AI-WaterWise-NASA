# 🌱 AI WaterWise Kerala

### NASA-Based AI Farming, Water Management and Environmental Monitoring System



## 🌍 Introduction

AI WaterWise Kerala is an AI-powered environmental monitoring and smart farming support system developed using NASA POWER satellite-based weather data.

The project analyzes historical rainfall and temperature patterns across 14 districts of Kerala to identify unusual weather conditions and assess potential drought risks.

Using Artificial Intelligence and data visualization, the system provides district-wise weather insights, drought risk categories, and useful recommendations for farmers.

The main aim of this project is to support sustainable agriculture, better water management, and climate resilience in Kerala.


## ❗ Problem Statement

Climate change and irregular rainfall patterns create challenges for agriculture and water management in Kerala.

Farmers may face difficulties in understanding changing rainfall patterns, unusual temperature conditions, and possible dry periods.

There is a need for an accessible system that uses historical environmental data to identify unusual weather patterns and provide useful information for better agricultural planning.


## 🎯 Objectives

- To analyze historical rainfall and temperature data across 14 districts of Kerala.
- To utilize NASA POWER data for environmental monitoring.
- To identify unusual weather patterns using Artificial Intelligence.
- To assess potential drought risks based on rainfall anomalies.
- To provide useful recommendations for farmers.
- To support sustainable agriculture and efficient water management.
- To develop an interactive dashboard for district-wise weather analysis.


## ✨ Key Features

- **14 Kerala Districts:** District-wise environmental data analysis.
- **NASA POWER Data:** Uses NASA satellite-based weather data.
- **AI Anomaly Detection:** Identifies unusual weather patterns using the Isolation Forest algorithm.
- **Drought Risk Assessment:** Estimates potential drought risk using rainfall anomalies and AI results.
- **Weather Visualization:** Displays rainfall and temperature charts.
- **Farmer Recommendations:** Provides useful suggestions based on weather conditions.
- **Interactive Dashboard:** Allows users to select districts and years for analysis.


## 💻 Technologies Used

- **Python:** Main programming language.
- **Google Colab:** Data analysis and model development.
- **Pandas:** Data cleaning and processing.
- **NumPy:** Numerical calculations.
- **Scikit-learn:** AI anomaly detection using Isolation Forest.
- **Streamlit:** Interactive web application development.
- **Plotly:** Interactive charts and visualizations.
- **NASA POWER API:** Historical rainfall and temperature data.
- **GitHub:** Project code and version control.


## 🛰️ NASA Data Source

This project uses historical weather data from **NASA POWER (Prediction Of Worldwide Energy Resources)**.

NASA POWER provides environmental data such as:
- Rainfall (Precipitation)
- Temperature
- Other meteorological parameters

The collected data is used to analyze rainfall and temperature patterns across 14 districts of Kerala.

**Official NASA POWER Website:**  
https://power.larc.nasa.gov/


## ⚙️ Methodology

The project follows these steps:

1. **Data Collection:** Collect historical rainfall and temperature data from NASA POWER API for 14 districts of Kerala.

2. **Data Preprocessing:** Clean and organize the collected weather data using Python and Pandas.

3. **Monthly Data Analysis:** Calculate monthly rainfall and temperature values.

4. **AI Anomaly Detection:** Apply the Isolation Forest algorithm to identify unusual weather patterns.

5. **Rainfall Anomaly Analysis:** Compare rainfall values with historical patterns to identify rainfall deviations.

6. **Drought Risk Assessment:** Estimate potential drought risk using rainfall anomalies and AI detection results.

7. **Farmer Recommendations:** Generate useful recommendations based on the identified weather conditions.

8. **Dashboard Development:** Display the results through an interactive Streamlit dashboard.


## 🏗️ System Architecture

The system follows a simple workflow to analyze environmental data and provide useful information to farmers.

### Working Flow

NASA POWER API  
⬇️  
Weather Data Collection  
⬇️  
Data Preprocessing  
⬇️  
Monthly Rainfall and Temperature Analysis  
⬇️  
Isolation Forest Anomaly Detection  
⬇️  
Drought Risk Assessment  
⬇️  
Farmer Recommendations  
⬇️  
Interactive Streamlit Dashboard

### Architecture Description

1. NASA POWER API provides historical weather data.
2. Python processes and organizes the collected data.
3. The AI model identifies unusual weather patterns.
4. The drought risk assessment module estimates potential dry conditions.
5. Farmer recommendations are generated based on the analysis.
6. Streamlit displays the results through an interactive dashboard.

