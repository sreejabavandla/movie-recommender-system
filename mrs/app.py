import streamlit as st # type: ignore

st.title("movie recommender system")

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))

st.write("You selected:", option)
