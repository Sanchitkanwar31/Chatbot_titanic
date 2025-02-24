
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("./dataset/clean_titanic_dataset.csv")

# Ensure the static directory exists to save images
os.makedirs("static", exist_ok=True)

def generate_plot(column):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=20, kde=True)
    plt.xlabel(column)
    plt.title(f"Distribution of {column}")
    
    image_path = f"static/{column}_distribution.png"
    plt.savefig(image_path)
    plt.close()
    return image_path

def generate_line_plot(column):
    plt.figure(figsize=(8, 5))
    df_sorted = df.sort_values(by=column)
    plt.plot(df_sorted[column].values, label=column, marker='o')
    plt.xlabel("Index")
    plt.ylabel(column)
    plt.title(f"Trend of {column}")
    plt.legend()
    
    image_path = f"static/{column}_trend.png"
    plt.savefig(image_path)
    plt.close()
    return image_path

def generate_countplot(column):
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df[column])
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.title(f"Count of {column}")
    
    image_path = f"static/{column}_count.png"
    plt.savefig(image_path)
    plt.close()
    return image_path

def generate_survival_by_class():
    plt.figure(figsize=(8, 5))
    survival_rates = df.groupby("Pclass")["Survived"].mean()
    sns.barplot(x=survival_rates.index, y=survival_rates.values)
    plt.xlabel("Passenger Class")
    plt.ylabel("Survival Rate")
    plt.title("Survival Rate by Passenger Class")
    
    image_path = "static/survival_by_class.png"
    plt.savefig(image_path)
    plt.close()
    return image_path

def generate_pclass_piechart():
    class_counts = df["Pclass"].value_counts()
    labels = [f"Class {c}" for c in class_counts.index]

    plt.figure(figsize=(6, 6))
    plt.pie(class_counts, labels=labels, autopct="%1.1f%%", colors=["gold", "skyblue", "lightcoral"], startangle=140)
    plt.title("Passenger Distribution by Class")

    image_path = "static/pclass_piechart.png"
    os.makedirs("static", exist_ok=True)
    plt.savefig(image_path)
    plt.close()

    return image_path










#EXTRA practice code 



#Updated in class to show graph table
# import os
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# # Load dataset
# df = pd.read_csv("./dataset/clean_titanic_dataset.csv")

# # Ensure the static directory exists
# os.makedirs("static", exist_ok=True)

# def save_plot(filename):
#     """ Helper function to save and close the plot """
#     filepath = f"static/{filename}"
#     plt.savefig(filepath)
#     plt.close()
#     return filepath

# def generate_plot(feature):
#     """ Generates a histogram for a given feature """
#     plt.figure(figsize=(6, 4))
#     plt.title(f"Distribution of {feature}")
#     sns.histplot(df[feature].dropna(), bins=10, kde=True)
#     return save_plot(f"{feature.lower()}_distribution.png")

# def generate_line_plot(feature):
#     """ Generates a line plot for a given feature """
#     plt.figure(figsize=(6, 4))
#     plt.plot(df.index, df[feature], marker='o', linestyle='-', color='b')
#     plt.title(f"Trend of {feature}")
#     plt.xlabel("Index")
#     plt.ylabel(feature)
#     plt.grid(True)
#     return save_plot(f"{feature.lower()}_trend.png")

# # def generate_age_distribution():
#     """ Generates the age distribution plot with survival information """
#     plt.figure(figsize=(6, 4))
#     plt.title("Age Distribution of Passengers on the Titanic")
#     sns.histplot(data=df, x="Age", hue="Survived", stat="density", common_norm=False, kde=True)
#     plt.xlabel("Age")
#     plt.ylabel("Density")
#     plt.legend(title="Survival", labels=["Not Survived", "Survived"])
#     return save_plot("age_distribution.png")

# #def generate_survival_count():
#     """ Generates a count plot for survival status """
#     plt.figure(figsize=(6, 4))
#     plt.title("Survival Count")
#     sns.countplot(x=df["Survived"], palette="pastel")
#     plt.xticks([0, 1], ["Not Survived", "Survived"])
#     plt.xlabel("Survival Status")
#     plt.ylabel("Count")
#     return save_plot("survival_count.png")

# # def generate_age_survival():
#     """ Compares age distributions of survivors vs non-survivors """
#     plt.figure(figsize=(6, 4))
#     sns.histplot(df[df["Survived"] == 1]["Age"], bins=20, kde=True, label="Survived", color="green")
#     sns.histplot(df[df["Survived"] == 0]["Age"], bins=20, kde=True, label="Not Survived", color="red")
#     plt.title("Age Distribution of Survivors vs Non-Survivors")
#     plt.xlabel("Age")
#     plt.ylabel("Count")
#     plt.legend()
#     return save_plot("age_survival.png")

# def generate_survival_by_class():
#     """ Generates a bar plot showing survival rate by passenger class """
#     plt.figure(figsize=(6, 4))
#     sns.barplot(x="Pclass", y="Survived", data=df, ci=None, palette="pastel")
#     plt.title("Survival Rate by Passenger Class")
#     plt.xlabel("Passenger Class")
#     plt.ylabel("Survival Rate")
#     return save_plot("survival_by_class.png")

# #def generate_fare_survival():
#     """ Generates a box plot of fares paid by survival status """
#     plt.figure(figsize=(6, 4))
#     sns.boxplot(x="Survived", y="Fare", data=df, palette="pastel")
#     plt.xticks([0, 1], ["Not Survived", "Survived"])
#     plt.title("Fare Distribution by Survival Status")
#     plt.xlabel("Survival Status")
#     plt.ylabel("Fare")
#     return save_plot("fare_survival.png")


