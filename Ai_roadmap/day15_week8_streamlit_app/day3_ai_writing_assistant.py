import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os 

topic = ""
load_dotenv()
api_key = os.getenv("GROQ")
client = Groq(api_key=api_key)
if "response" not in st.session_state:
    st.session_state.response = ""
topic = st.text_input("Enter your topic")
tone = st.selectbox(label="Select tone",options=["formal","casual","funny","Angry"])
if st.button("Generate"):
    if topic == "":
        st.write("Warning!! Topic cannot be empty")
    else:
        output = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {"role":"system","content":"Adjust your behaviour according to the tone give by user and answer the topic."},
                {"role":"user","content":f'''{topic},Use the {tone} tone to generate the output'''}
            ]
        )
        st.session_state.response = output.choices[0].message.content
if st.session_state.response:
    st.write(st.session_state.response)