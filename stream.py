import streamlit as st
from datetime import datetime

from ai import generate_menu
from db import save_menu

st.title("Kantine AI - Ugeplan generator")

antal = st.slider("Antal personer", 20, 500, 120)
budget = st.slider("Budget pr kuvert", 20, 80, 45)
vegetar = st.checkbox("Vegetar ønskes", True)
fisk = st.checkbox("Fisk tilladt", True)

if st.button("Generér menu med AI"):
    menu = generate_menu(antal, budget, vegetar, fisk)

    st.subheader("Forslag til menu")

    for dag, ret in menu.items():
        st.write(f"**{dag}:** {ret}")

    uge = datetime.now().isocalendar()[1]
    år = datetime.now().year

    save_menu(uge, år, menu, budget, antal)

    st.success("Menu gemt i database!")
