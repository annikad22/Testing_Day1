import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
st.title ("Roma's World")
if "Roma" not in st.session_state:
    st.session_state.name = "Roma"
if "button_value" not in st.session_state:
    st.session_state.button_value = False
if "option" not in st.session_state:
    st.session_state.option = "Roma"
    #ask user to enter name
st.header("Part 1 - Get Name")
st.session_state.name=st.text_input("What's your name?")
#If user enters their name and licks a button
st.header("Part 2 - Click Button")
st.session_state.button_value = st.button("Click Me")
st.header("Part 3 - Display Name (Hardcoded)")
if st.session_state.name !=" " and st.session_state.button_value:
    st.write(f"Hello, {st.session_state.name}")
