import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("./dataset/clean_titanic_dataset.csv")

def generate_plot(feature):
    plt.figure(figsize=(6,4))
    plt.title(f"Distribution of {feature}")
    sns.histplot(df[feature], bins=10,kde=True)
    plt.savefig("plot.png")
    plt.close()

    return "plot.png"

def generate_line_plot(feature):
    plt.figure(figsize=(6, 4))
    plt.plot(df.index, df[feature], marker='o', linestyle='-', color='b')  # Line with markers
    plt.title(f"Trend of Line {feature}")
    plt.xlabel("Index")
    plt.ylabel(feature)
    plt.grid(True)  # Adds a grid for better readability
    plt.savefig("line_plot.png")
    plt.close()
    
    return "line_plot.png"
