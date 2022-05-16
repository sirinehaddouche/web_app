import streamlit as st 
import pandas as pd 
import plotly_express as px
#import mymodel as m 

st.title("Welcome the the web app about COVID 19")
st.write("""
# COVID-19 Dashboard
Below you will find our dashbord that is updated every day.
""")


df = pd.read_csv('https://static.data.gouv.fr/resources/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/20220513-190143/covid-hospit-etab-2022-05-13-19h01.csv', sep = ';')
df

#st.line_chart(df.plot())


selectbox = st.sidebar.selectbox(
    "Select the one you want",
    ["Vaccinated", "No Vacinnated"]
)
st.write(f"You selected {selectbox}")

fig2 = px.line(df, x='jour', y='nb')
ts_chart = st.plotly_chart(fig2)