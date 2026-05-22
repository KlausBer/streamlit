import streamlit as st
from anthropic import Anthropic


st.title("🍽️ Kantine AI - Uge menu (Claude)")

client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

# INPUTS
antal = st.slider("Antal personer", 20, 500, 120)
budget = st.slider("Budget pr. kuvert (kr)", 20, 80, 45)

vegetar = st.checkbox("Mindst 1 vegetarret", True)
fisk = st.checkbox("Fisk tilladt", True)

stil = st.selectbox(
    "Madstil",
    ["klassisk dansk", "sund", "comfort food", "varieret", "budgetvenlig"]
)

if st.button("Generér menu med Claude"):
    
    prompt = f"""
Du er en erfaren kantinekok.

Lav en uge-menu (mandag til fredag).

Krav:
- {antal} personer
- budget: {budget} kr pr kuvert
- vegetar: {vegetar}
- fisk tilladt: {fisk}
- stil: {stil}
- dansk kantinemad
- god variation gennem ugen

Svar KUN i dette format:

Mandag: ...
Tirsdag: ...
Onsdag: ...
Torsdag: ...
Fredag: ...
"""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=800,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    st.subheader("📋 Forslag til uge-menu")
    st.text(message.content[0].text)
