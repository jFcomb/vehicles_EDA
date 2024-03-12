import pandas as pd
import streamlit as st
import plotly_express as px

# Layout config
st.set_page_config(layout="wide")

# Title
st.title("Análisis exploratorio")
st.subheader("Dataset preprocesado")

# Read csv
df = pd.read_csv(
    "https://github.com/jFcomb/vehicles_EDA/blob/main/prep_vehicles_us.csv?raw=true", index_col=0)
st.dataframe(df, use_container_width=True)

# Vehicle by condition
st.subheader("Cantidad de vehículos según la condición")
fig = px.bar(df, x='condition', height=400)
st.plotly_chart(fig)

# Vehicles type by manufacturer
st.write("Cantidad de tipo de vehículos según marca")
fig_2 = px.bar(df.groupby(['type', 'model'])['model'].agg('count'))
st.plotly_chart(fig_2, use_container_width=True)
