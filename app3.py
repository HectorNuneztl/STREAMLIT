import numpy as np
import pandas as pd
import streamlit as st

st.title(":red[MY FIST APP]")

# ORIGINAL TABLE
st.header("ORIGINAL TABLE: ", divider="red")

dataFrame = pd.read_csv("internet_usage.csv")
st.write(dataFrame)

# Display top 5 countries by internet usage in 2023 (table and bar chart)#
st.subheader("Top 5 countries by internet usage in 2023", divider="green")

# filter for column 2023
info23 = dataFrame.loc[:, ["Country Name", "Country Code", "2023"]]
info23 = info23[info23["2023"] > "0"]  # discard columns without a numeric sequence
st.write(info23)

# filter for 5 max values from the df
info23["2023"] = pd.to_numeric(info23["2023"])
MaxValues_23 = info23.nlargest(5, "2023").sort_values("2023", ascending=True)

# table (Top 5)
st.write(MaxValues_23)

# chart (Top 5)
st.line_chart(MaxValues_23, x="Country Name", y="2023")


# Visualize internet usage in North America Counties (line chart) - from 2013 to 2023
st.subheader("Internet usage in NA countries (2013-2023): ", divider="blue")

# filter north america countries
info_NthAm = dataFrame[
    dataFrame["Country Name"].isin(
        [
            "Barbados",
            "Belize",
            "Bermuda",
            "Canada",
            "Costa Rica",
            "Cuba",
            "Dominica",
            "Dominican Republic",
            "El Salvador",
            "Grenada",
            "Guatemala",
            "Haiti",
            "Honduras",
            "Jamaica",
            "Mexico",
            "Nicaragua",
            "Panama",
            "St. Kitts and Nevis",
            "St. Lucia",
            "St. Vincent and the Grenadines",
            "Trinidad and Tobago",
            "United States",
        ]
    )
]

# filter from 2013-2023
targetYear = [
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
]

info_NthAm = info_NthAm.loc[
    :,
    [
        "Country Name",
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
        "2018",
        "2019",
        "2020",
        "2021",
        "2022",
        "2023",
    ],
]

# line chart
st.line_chart(info_NthAm, x="Country Name", y=targetYear)

# Add a filter (input widget: multiselect) with values "USA, Mexico, Canada" for filtering line chart
st.subheader("Filter for USA, MEXICO and CANADA: ", divider="blue")

targetCount = ["United States", "Mexico", "Canada"]
info_targetCount = info_NthAm[info_NthAm["Country Name"].isin(targetCount)]

# Table (USA, MEXICO, CANADA)
st.write(info_targetCount)
options = st.multiselect("OPTIONS: ", targetCount, default=targetCount)

# chart (USA, MEXICO, CANADA)
st.line_chart(
    info_targetCount[info_targetCount["Country Name"].isin(options)],
    x="Country Name",
    y=targetYear,
)


# Calculate growth rate for period 2021-2022 (add new column to current DataFrame using pandas,  column name example: "growth_rate_2023")
st.subheader("Growth 2021-2022", divider="violet")

dataFrame["2021"] = dataFrame["2021"].replace("..", 0).astype(float)
dataFrame["2022"] = dataFrame["2022"].replace("..", 0).astype(float)
dataFrame["growth"] = (
    (dataFrame["2022"] - dataFrame["2021"]) / dataFrame["2021"]
) * 100
st.write(dataFrame.loc[:, ["Country Name", "2021", "2022", "growth"]])

# Display top 5 countries by "growth_rate_2023" (bar chart)
st.subheader("Top 5: ", divider="violet")
dataFrame = dataFrame.nlargest(5, "growth")
st.write(dataFrame.loc[:, ["Country Name", "2021", "2022", "growth"]])
