import streamlit as st

st.title("AI Research Assistant")

query = st.text_input("Ask question about research paper")

if query:
    st.write("Searching research papers...")