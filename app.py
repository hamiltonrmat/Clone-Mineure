import streamlit as st

# 2. On utilise une fonction de Streamlit pour afficher du texte
# st.title() affiche le texte comme un titre principal
st.title("Bonjour à tous !")

d = {'Col1': ['toi', 'moi'], 'Col2': [1, 2]}

st.dataframe(d)
