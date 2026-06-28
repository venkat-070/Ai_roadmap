import streamlit as st
if "response" not in st.session_state:
    st.session_state.response = ""
st.title("Session State")
name = st.text_input("Enter your name: ")
if st.button("Save Name"):
    st.session_state.response = name
st.write("Saved Name:",st.session_state.response)
