
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI WaterWise Kerala",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI WaterWise Kerala")
st.subheader(
    "NASA-Based AI Farming, Water Management "
    "and Environmental Monitoring System"
)

st.markdown("""
This dashboard analyzes NASA POWER historical rainfall
and temperature data for 14 districts of Kerala.
""")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("AI_WaterWise_Kerala_Final_Results.csv")

try:
    df = load_data()
except Exception:
    st.error("Dataset not found. Please upload the CSV file to GitHub.")
    st.stop()

# Sidebar
st.sidebar.title("Dashboard Filters")

districts = sorted(df["Location"].unique())

selected_district = st.sidebar.selectbox(
    "Select Kerala District",
    districts,
    index=districts.index("Palakkad")
)
district_df = df[
    df["Location"] == selected_district
].copy()

years = sorted(district_df["Year"].unique())

selected_year = st.sidebar.selectbox(
    "Select Year",
    years,
    index=len(years) - 1
)

filtered_df = district_df[
    district_df["Year"] == selected_year
].copy()

st.header(f"📍 {selected_district} - {selected_year}")

# Key metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Temperature",
    f'{filtered_df["Temperature_C"].mean():.2f} °C'
)

col2.metric(
    "Total Rainfall",
    f'{filtered_df["Rainfall_mm"].sum():.2f} mm'
)

col3.metric(
    "Unusual Weather Records",
    int((filtered_df["AI_Status"] == "Unusual Condition").sum())
)

st.divider()

# Rainfall chart
st.subheader("🌧️ Monthly Rainfall Analysis")

fig1 = px.bar(
    filtered_df,
    x="Month",
    y="Rainfall_mm",
    title="Monthly Rainfall",
    labels={
        "Month": "Month",
        "Rainfall_mm": "Rainfall (mm)"
    }
)

st.plotly_chart(fig1, use_container_width=True)

# Temperature chart
st.subheader("🌡️ Temperature Analysis")

fig2 = px.line(
    filtered_df,
    x="Month",
    y="Temperature_C",
    markers=True,
    title="Monthly Average Temperature"
)

st.plotly_chart(fig2, use_container_width=True)

# Drought risk pie chart
st.subheader("🥧 Drought Risk Distribution")

risk_counts = filtered_df["Drought_Risk"].value_counts().reset_index()
risk_counts.columns = ["Drought_Risk", "Count"]

fig3 = px.pie(
    risk_counts,
    names="Drought_Risk",
    values="Count",
    title="Drought Risk Categories"
)

st.plotly_chart(fig3, use_container_width=True)

# AI anomaly analysis
st.subheader("🤖 AI Weather Anomaly Detection")

anomaly_counts = filtered_df["AI_Status"].value_counts().reset_index()
anomaly_counts.columns = ["AI_Status", "Count"]

fig4 = px.bar(
    anomaly_counts,
    x="AI_Status",
    y="Count",
    title="Normal vs Unusual Weather Conditions"
)

st.plotly_chart(fig4, use_container_width=True)

# Farmer recommendations
st.subheader("🌾 Farmer Recommendations")

for _, row in filtered_df.iterrows():
    st.write(
        f'**Month {int(row["Month"])} – '
        f'{row["Drought_Risk"]}:** '
        f'{row["Farmer_Recommendation"]}'
    )

# Data table
with st.expander("View Detailed Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

# Disclaimer
st.divider()

st.caption("""
Data Source: NASA POWER.
Each district is represented by one selected coordinate.
AI anomaly detection and drought risk categories are
experimental prototype results, not official drought forecasts.
""")

st.success("AI WaterWise Kerala Dashboard Loaded Successfully!")

