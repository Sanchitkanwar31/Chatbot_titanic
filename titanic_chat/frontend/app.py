import streamlit as st
import requests

st.title("⚓ AI Titanic Captain")

query = st.text_input("Ask me anything about the Titanic dataset")  
if st.button("Submit"):
    res = requests.get(f"http://127.0.0.1:8000/query/?question={query}").json()
    print(res.text) 
    st.write(res["response"])

    if res["visualization"]:
        st.image(res["plot.png"])
        st.image(res["line_plot.png"])
        