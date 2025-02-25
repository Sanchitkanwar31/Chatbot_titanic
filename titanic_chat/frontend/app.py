# import streamlit as st
# import requests

# st.title("⚓ AI Titanic Captain")

# BASE_URL = "http://127.0.0.1:8000"

# # fetch data from /summary/ url
# if st.sidebar.button("Show Dataset Summary"):
#     res = requests.get(f"{BASE_URL}/summary/").json()
#     st.sidebar.subheader("Dataset Summary")
#     st.sidebar.write(f"**Total Passengers:** {res['total_passengers']}")
#     st.sidebar.write(f"**Survival Rate:** {res['survival_rate']:.2%}")
#     st.sidebar.write(f"**Average Age:** {int(res['average_age'])} **years**")
#     #st.sidebar.write(f"**Class Distribution:**")
#     #st.sidebar.json(res["class_distribution"])


# query = st.text_input("Ask me anything about the Titanic dataset")  
# if st.button("Submit"):
#     res = requests.get(f"http://127.0.0.1:8000/query/?question={query}").json()
#     st.write(res["response"])

#     if "visualization" in res and res["visualization"]:
#         # st.image(res["plot.png"])
#         # st.image(res["line_plot.png"])
#         st.image(res["visualization"], caption="Generated Visualization")
        

import streamlit as st
import requests

import os
import streamlit as st

# Ensure secrets are loaded
# if "GEMINI_API_KEY" not in st.secrets:
#     st.error("GEMINI_API_KEY is missing in Streamlit secrets!")
# else:
#     GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]


st.title("⚓ AI Titanic Captain")





BASE_URL = "http://127.0.0.1:8000"

#BASE_URL = "https://aicaptainchatbot-sanchit31.herokuapp.com"

#fetch data from /summary/ url
if st.sidebar.button("Show Dataset Summary"):
    res = requests.get(f"{BASE_URL}/summary/").json()
    st.sidebar.subheader("Dataset Summary")
    st.sidebar.write(f"**Total Passengers:** {res['total_passengers']}")
    st.sidebar.write(f"**Survival Rate:** {res['survival_rate']:.2%}")
    st.sidebar.write(f"**Average Age:** {int(res['average_age'])} **years**")
    #st.sidebar.write(f"**Class Distribution:**")
    #st.sidebar.json(res["class_distribution"])


query = st.text_input("Ask me anything about the Titanic dataset")  
if st.button("Submit"):
    response = requests.get(f"http://127.0.0.1:8000/query/?question={query}").json()

    st.write(response["response"])

    # Check if visualization is returned
    if response.get("visualization"):
        st.image(response["visualization"], caption="Generated Visualization", use_column_width=True)
