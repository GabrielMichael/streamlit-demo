import streamlit as st

st.title("Demo App")
user_selection = st.sidebar.radio("Yes or no", ["yes", "no"])
if st.button("click to see what user selected"):
    st.write(f"User selected {user_selection}")
