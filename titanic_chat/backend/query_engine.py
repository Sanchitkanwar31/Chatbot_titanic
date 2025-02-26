
import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
from backend.visualization import (
    generate_pclass_piechart,
    generate_plot,
    generate_line_plot,
    generate_countplot,
    generate_survival_by_class,
)

# Setup environment variable
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing! Check your .env file.")

genai.configure(api_key=api_key)


def query_titanic_data(question):
    visualization = None
    image_path = None

    if "age distribution" in question.lower() or "Show me a histogram of passenger ages" in question.lower() or "age graph" in question.lower():
        image_path = generate_plot("Age")
    elif "fare trend" in question.lower():
        image_path = generate_line_plot("Fare")
    elif "survival by class" in question.lower():
        image_path = generate_survival_by_class()
    elif "passenger class distribution" in question.lower() or "pie chart" in question.lower():
        image_path = generate_pclass_piechart()
        
    
    
    if image_path:
        return "Here is the requested visualization", image_path


    prompt = f"In this Titanic dataset: {question}"
    model = genai.GenerativeModel("gemini-1.5-pro")  
    response = model.generate_content(prompt)
    return response.text, visualization
