import pandas as pd
import streamlit as st
import plotly_express as px

# Layout config and initial config
st.set_page_config(layout="wide")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

# Title
st.title("Explorarory Data Analist")
st.subheader("Dataset")

# Read csv
df = pd.read_csv(
    "https://github.com/jFcomb/vehicles_EDA/blob/main/prep_vehicles_us.csv?raw=true", index_col=0)
st.dataframe(df, use_container_width=True)

################ Vehicle by condition #############################
st.subheader("Number of vehicles per condition")  # Title
df_temp = df.groupby(by='condition', as_index=False)[
    'price'].count()  # Creation of number of cars by condition
fig = px.bar(df_temp, x='condition', y='price', labels={
             'price': 'count'}, text_auto=True)  # Creation of bar graphic
st.plotly_chart(fig, use_container_width=True)  # Display graphic

################# Vehicles type by manufacturer ######################
st.subheader("Vehicles type by manufacturer")
# Selectbox creation
options = ['Vehicles by manufacturer',
           'Vehicles type by manufacturer']  # Options to be displayed
chart_option = st.selectbox(
    'Select an option', options)  # Option chosen

if chart_option == options[0]:
    df_temp = df.groupby(by='company', as_index=False)[
        'price'].count()  # Creation of number of cars by company
    fig = px.bar(df_temp,
                 x='company',
                 y='price',
                 labels={'price': 'count'},
                 text_auto=True,
                 height=600
                 )  # Creation of bar graphic
elif chart_option == options[1]:
    df_temp = df.groupby(['company', 'type'], as_index=False)['price']\
        .count().rename(columns={'price': 'count'})  # Creation of number of cars by type
    fig = px.bar(df_temp,
                 x='company',
                 y='count',
                 color='type',
                 height=600
                 )  # Creation of bar graphic
st.plotly_chart(fig, use_container_width=True)

############## Distribution campare between manufacturers ##################
st.subheader("Distribution compare between manufacturers")
# Columns creation
col1, col2 = st.columns(2)
options = df['company'].unique()  # Options to be displayed
with col1:
    company_sbox1 = st.selectbox('Select first manufacturer',
                                 options=options)
with col2:
    company_sbox2 = st.selectbox('Select second manufacturer',
                                 options=options,
                                 index=1)
# Checkbox creation
chkbox = st.checkbox('Normalize histogram', value=True)
if chkbox == True:
    histnorm = 'percent'
else:
    histnorm = None

df_query = df.query(
    "company == @company_sbox1 or company == @company_sbox2")  # Filter Data
# Histogram Creation
fig = px.histogram(df_query,
                   x='price',
                   color='company',
                   opacity=0.7,
                   histnorm=histnorm,
                   nbins=50,
                   height=700,
                   )

st.plotly_chart(fig, use_container_width=True)
