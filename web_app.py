import streamlit as st 
import pandas as pd 
import plotly_express as px
#import mymodel as m 

st.title("Bienvenue sur l'application web à propos de la crise du Covid 19 en France")
st.write("""
# Il s'agit d'un dashboard intéractif qui traite des données misent à jour en temps réél. Vous pouvez naviguer sur l'interface à l'aide de votre souris :)
""")


df = pd.read_csv('https://static.data.gouv.fr/resources/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19/20210202-220106/vaccination-regional.csv', sep = ',')
df['date'] = pd.to_datetime(df['date'])
#st.line_chart(df.plot())
df['jour_semaine'] = df['date'].dt.day_name()
df['total_deaths'] = 10



categories_count = ['total_vaccines', 'total_deaths']
chosen_count = st.sidebar.selectbox(
   'Que choisissez_vous ?',
   categories_count
)
fig3 = px.box(df, x='jour_semaine', y=chosen_count, notched=True)
boxplot_chart = st.plotly_chart(fig3)

selectbox = st.sidebar.selectbox(
    "Select the one you want",
    ["Vaccinated", "Not Vacinnated"]
)
#st.write(f"You selected {selectbox}")

#fig2 = px.line(df, x='jour', y='nb')
#ts_chart = st.plotly_chart(fig2)

