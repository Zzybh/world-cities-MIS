import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Title
st.title("California Housing Data (1990) by Zhao Ziyu")


# Load data
df = pd.read_csv("housing.csv")


# Slider
house_value_filter = st.slider(
    "Minimal Median House Value",
    0,
    500001,
    200000
)


# Sidebar title
st.subheader("See more filters in the sidebar:")


# Sidebar: ocean proximity filter
location_filter = st.sidebar.multiselect(
    "Choose the location type",
    df["ocean_proximity"].unique(),
    df["ocean_proximity"].unique()
)


# Sidebar: income level filter
income_filter = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)


# Filter by house value
df = df[df["median_house_value"] >= house_value_filter]


# Filter by location
df = df[df["ocean_proximity"].isin(location_filter)]


# Filter by income
if income_filter == "Low":
    df = df[df["median_income"] <= 2.5]

elif income_filter == "Medium":
    df = df[
        (df["median_income"] > 2.5) &
        (df["median_income"] < 4.5)
    ]

elif income_filter == "High":
    df = df[df["median_income"] >= 4.5]


# Show map
st.subheader("Housing District Map")
st.map(
    df[
        [
            "latitude",
            "longitude"
        ]
    ]
)


# Show histogram
st.subheader("Median House Value Distribution")

fig, ax = plt.subplots()

ax.hist(
    df["median_house_value"],
    bins=30
)

ax.set_xlabel("Median House Value")
ax.set_ylabel("Number of Districts")

st.pyplot(fig)