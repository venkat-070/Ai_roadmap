import streamlit as st
st.title("AI Writing Assistant")
topic = st.text_input(label="Enter your topic here:")
tone = st.selectbox(label = "Select a tone:",options=["formal","casual","funny"])
if st.button("Generate"):
    st.write("You selected:",tone,"the topic:",topic)

