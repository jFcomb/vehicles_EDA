import pandas as pd
import streamlit as st
import plotly_express as px

# Read csv
df = st.dataframe(
    'C:/Users/jfcom/Documents/modulo_adicional/proyecto/vehicles_EDA-2/prep_vehicles_us.csv')

st.write(df)
