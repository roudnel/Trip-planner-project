import streamlit as st
import pandas as pd


st.title("Trip Planner")
st.header(" Lieux à visiter, le mois pour partir, et ou partir ")
st.write(" Voici votre choix")


st.write("Data source: [Ou et quand partir] https://www.ou-et-quand.net/partir/quand/"+ "  "+ "     "+  "https://generationvoyage.fr" +" " +"https://partir.ouest-france.fr/meteo/oupartiren")
    
data =pd.read_csv('C:/Users/Laetitia/OneDrive/Documents/MS dS2E/Projet Kevin/Trip-planner-project-main/trip_ planner.csv')
st.dataframe(data)


st.write("Hugo Leonard", "Laetitia Santos Moreira", "Roudnel Colin")
