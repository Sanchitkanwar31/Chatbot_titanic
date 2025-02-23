from fastapi import FastAPI
from backend.query_engine import query_titanic_data
import pandas as pd
app = FastAPI()

df = pd.read_csv("./dataset/clean_titanic_dataset.csv")

@app.get("/")
def home():
    return {"message":"Titanic Chatbot running"}


@app.get("/query/")
def query(question: str):
    response, visualization = query_titanic_data(question)  
    return {"response":response, "visualization":visualization}


# @app.get("/passenger/{id}")
# def get_passenger(id: int):
#     passenger = df[df["PassengerId"] == id]
#     if passenger.empty:
#         raise HTTPException(status_code=404, detail="Passenger not found")
#     return passenger.to_dict(orient="records")[0]


@app.get("/summary/")
def dataset_summary():
    summary = {
        "total_passengers": len(df),
        "survival_rate": df["Survived"].mean(),
        "average_age": df["Age"].mean(),
        "class_distribution": df["Pclass"].value_counts().to_dict()
    }
    return summary