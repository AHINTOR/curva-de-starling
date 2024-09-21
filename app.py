import streamlit as st
import patient_equations as eq
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Curva de Frank Starling")
st.markdown("_Adaptado por ***Jorge Quispe***:_")

# --- PAGE SETUP ---
about_page = st.Page(
    "pages/formula.py",
    title="Curva Frank Starling",
    icon=":material/monitoring:",
    default=True,
)
project_1_page = st.Page(
    "pages/problema.py",
    title="Problema",
    icon=":material/problem:",
)
project_2_page = st.Page(
    "pages/referencias.py",
    title="Referencias",
    icon=":material/developer_guide:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "App": [about_page],
        "Documentación": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("images/starling_rap.svg")
st.sidebar.markdown("Hecho con **python y streamlit** en el curso de _Cuadernos de código Python_ ❤️ by [Ahintor](https://anestesia.wiki)")


# --- RUN NAVIGATION ---
pg.run()
