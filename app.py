import pandas as pd
import streamlit as st
import plotly_express as px

button = st.button('botón de prueba')
# Title

st.title("Análisis exploratorio")
st.subheader("Tabla preprocesada")

# Read csv
df = pd.read_csv(
    "https://github.com/jFcomb/vehicles_EDA/blob/main/prep_vehicles_us.csv?raw=true", index_col=0)


st.dataframe(df)
