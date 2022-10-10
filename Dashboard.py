import streamlit as st
import pandas as pd

st.title("Trip Planner")
st.header(" Préparer vos valises, vous êtes prêt à partir!")
    
st.write(" Voici votre choix :")
    
liste = open(r'liste.txt', 'r')
lr = liste.read()
st.write(lr)
 
data =pd.read_csv('/Users/hugol/Advanced Programming/T2/trip_ planner.csv')
st.dataframe(data)
    
st.write("Hugo Leonard, ", "Laetitia Santos Moreira, ", "Roudnel Colin")
st.write("Data source: ")
st.write("https://www.ou-et-quand.net/ , https://www.tripadvisor.fr/ , https://partir.ouest-france.fr")
