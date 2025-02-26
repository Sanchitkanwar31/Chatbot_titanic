from fastapi import FastAPI
from backend.query_engine import query_titanic_data
import google.generativeai as genai
import matplotlib.pyplot as plt
import seaborn as sns   
import os
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (Streamlit Cloud) to access FastAPI backend
origins = [
    "https://aicaptainchatbot-sanchit31.streamlit.app",  # Your deployed Streamlit app
    "http://localhost",  # For local testing
    "http://127.0.0.1",  # Local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
                        
df = pd.read_csv("./dataset/clean_titanic_dataset.csv")

@app.get("/")
def home():
    return {"message":"Titanic Chatbot running"}



@app.get("/query/")
def query(question: str):
    response, visualization = query_titanic_data(question)
    return {"response": response, "visualization": visualization}


@app.get("/summary/")
def dataset_summary():
    summary = {
        "total_passengers": len(df),
        "survival_rate": df["Survived"].mean(),
        "average_age": df["Age"].mean(),
        #"class_distribution": df["Pclass "].value_counts().to_dict()
    }
    return summary

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
