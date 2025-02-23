import os
import pandas as pd
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

#setup environment variable
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing! Check your .env file.")


df = pd.read_csv("./dataset/clean_titanic_dataset.csv")
llm = ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=api_key)


def query_titanic_data(question):
    prompt = f"In this Titanic dataset: {question}"
    response = llm([SystemMessage(content=prompt)])
    return response.content, None  # Visualization to be added later