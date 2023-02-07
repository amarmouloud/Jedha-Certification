import streamlit as st

st.set_page_config(
    page_title="Getaround Delay Analysis",
    page_icon="🚗",
)

st.write("# Bienvenue dans l'analyse des retards Getaround! 👋")

st.sidebar.success("Sélectionnez une page ci-dessus.")

st.markdown(
    """
    Cette application a été conçue pour l'obtention de la certification Fullstack Data Science par Jedha

    ### De quoi s'agit-il?
    GetAround est l'Airbnb pour les voitures. Vous pouvez louer des voitures à n'importe qui pour quelques heures à quelques jours ! Fondée en 2009, cette entreprise a connu une croissance rapide. En 2019, ils comptent plus de 5 millions d'utilisateurs et environ 20 000 voitures disponibles dans le monde.
    
    Avec Getaround, les chauffeurs réservent des voitures pour une durée déterminée, d'une heure à quelques jours. Ils sont censés ramener la voiture à temps, mais il arrive de temps en temps que des chauffeurs soient en retard à la caisse.

    Le but de cette analyse est d'aider le chef de produit à décider de la durée minimale du délai entre les locations.


 
"""
)