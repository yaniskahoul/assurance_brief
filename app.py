import streamlit as st
import pickle
import pandas as pd
import numpy as np


# Charger le modèle depuis le fichier
pickle_in = open('my_pipe_lr.pkl', 'rb') 
my_pipe_lr = pickle.load(pickle_in)

st.title("Assur'Aimant")
st.subheader("Faites votre devis d'assurance en 2 minutes!")

# Ajout d'une image
#st.image(image = "/home/apprenant/Bureau/Brief-ML-Assurance/Assuraimant.jpeg")


# Demande des informations à l'utilisateur
age = st.number_input("Quel est votre âge?", min_value=18, max_value=120, value = 18)
sexe = st.radio("Quel est votre sexe?", ("male", "female"))
bmi = st.number_input("Quel est votre IMC?", min_value=10, max_value=50,value = 25)
nombre_enfants = st.number_input("Combien avez-vous d'enfants?", min_value=0, max_value=20)
fumeur = st.radio("Êtes-vous fumeur?", ("yes", "no"))
region = st.radio("De quel region êtes-vous?", ("southwest","southeast","northwest","northeast"))



liste = [int(age), sexe, bmi, int(nombre_enfants), fumeur, region]

liste_col = ['age', 'sex', 'bmi', 'children', 'smoker','region']

if st.button("Démarrez l'estimation"):
    df = pd.DataFrame(np.array(liste).reshape(1, -1),columns = liste_col)
    prediction = my_pipe_lr.predict(df)
    charges = int(my_pipe_lr.predict(df)[0])
    st.title("Votre estimation est de {} $".format(format(charges, '.2f')))