import streamlit as st
import random

st.title("Kantine AI - Uge menu generator")

# INPUTS
antal = st.slider("Antal kuverter", 20, 500, 120)
budget = st.slider("Budget pr. kuvert (kr)", 20, 80, 45)

vegetar = st.checkbox("Mindst 1 vegetarret", True)
fisk = st.checkbox("Tillad fisk", True)

# Simpel “mad database”
retter = [
    {"navn": "Lasagne", "type": "kød"},
    {"navn": "Kylling i karry", "type": "kød"},
    {"navn": "Frikadeller", "type": "kød"},
    {"navn": "Taco bar", "type": "kød"},
    {"navn": "Vegetar lasagne", "type": "vegetar"},
    {"navn": "Buddha bowl", "type": "vegetar"},
    {"navn": "Pasta pesto", "type": "vegetar"},
    {"navn": "Fiskefilet", "type": "fisk"},
]

uger = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]

def filtrer_retter():
    valgte = retter.copy()

    if not fisk:
        valgte = [r for r in valgte if r["type"] != "fisk"]

    return valgte

if st.button("Generér menu"):
    valgte = filtrer_retter()

    menu = []

    vegetar_brugt = False

    for dag in uger:
        mulige = valgte

        # tving vegetar hvis nødvendigt
        if vegetar and not vegetar_brugt:
            mulige = [r for r in mulige if r["type"] == "vegetar"]

        valg = random.choice(mulige)
        menu.append((dag, valg["navn"]))

        if valg["type"] == "vegetar":
            vegetar_brugt = True

    st.subheader("Forslag til uge-menu")

    for dag, ret in menu:
        st.write(f"**{dag}:** {ret}")

    st.info(f"Budget: {budget} kr pr kuvert | Kuverter: {antal}")
