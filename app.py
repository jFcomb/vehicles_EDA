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
st.subheader("Cantidad de tipo de vehículos por fabricante")

# Select box creation
options = ['Total de vehículos por marca',
           'Total de Vehículos por tipo y marca']

chart_option = st.selectbox('¿Qué gráfico quieres ver?', options, index=0)
st.write('You selected:', chart_option)
select_index = chart_option.index(chart_option)
st.write('You selected:', select_index)

# Company count by type table creation
ctt = df.groupby(['company', 'type'], as_index=False)['price']\
    .count().rename(columns={'price': 'count'})

# Vehicles type by manufacturer chart
fig_2 = px.bar(ctt, x='company', y='count', color='type')
st.plotly_chart(fig_2, use_container_width=True)
