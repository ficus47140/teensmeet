import streamlit as st

def page():
  s = ["Home", "Recherche", "proposition", "message"]
  x = st.sidebar.selectbox("Choisissez une option : ", s)
  return s.index(x)+1if x is not None else 1