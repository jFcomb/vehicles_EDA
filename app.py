import pandas as pd
import streamlit as st
import plotly_express as px

# Read csv
df = pd.read_csv(
    "https://github.com/jFcomb/vehicles_EDA/blob/main/prep_vehicles_us.csv?raw=true")
# df = pd.read_csv(
#    'C:/Users/jfcom/Documents/modulo_adicional/proyecto/vehicles_EDA/vehicles_us.csv')

st.dataframe(df)
