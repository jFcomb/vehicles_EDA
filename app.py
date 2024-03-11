import pandas as pd
import streamlit as st
import plotly_express as px

# Read csv
df = pd.read_csv('https://github.com/jFcomb/vehicles_EDA/blob/main/vehicles_us.csv')

st.dataframe(df)
