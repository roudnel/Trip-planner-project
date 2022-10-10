
import streamlit as st
import pandas as pd


st.title("Trip Planner")
st.header(" Préparer vos valises, vous êtes prêt à partir!")


st.write(" Voici votre choix")


data =pd.read_csv('C:/Users/Laetitia/OneDrive/Documents/MS dS2E/Projet Kevin/Trip-planner-project-main/trip_ planner.csv')
st.dataframe(data)


st.write("Hugo Leonard"+" , " +"Laetitia Santos Moreira"+" ,"+"Roudnel Colin")


st.write("Data source: [Ou et quand partir]  https://www.ou-et-quand.net/partir/quand/")
st.write("https://www.tripadvisor.fr/" )
st.write("https://partir.ouest-france.fr/meteo/oupartiren")
                
