# Chatbot_titanic
This my first project which has engaged my mind to work on the field of LLM and how openAI works .


# 🚢 AI Titanic Captain - Chatbot

## Overview
This project is an AI-powered chatbot that allows users to interact with the Titanic dataset using natural language queries. It provides both textual and graphical insights based on user queries. The chatbot is built using **FastAPI** for the backend, **Streamlit** for the frontend, and **Google Gemini AI** for query processing.

## Features
- 📊 Retrieve statistical insights from the Titanic dataset.
- 📈 Generate visualizations (histograms, line plots, pie charts, etc.).
- 🤖 Use Google Gemini AI to answer queries.
- 🖼️ Display graphs dynamically in the Streamlit frontend.

## Installation
### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-repo/titanic-chatbot.git
cd titanic-chatbot
```

### 2️⃣ Create and activate a virtual environment
```sh
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set up the environment variables
Create a **.env** file in the root directory and add:
```sh
GEMINI_API_KEY=your_google_gemini_api_key
```

## Running the Project
### 1️⃣ Run the FastAPI Backend
```sh
uvicorn backend.main:app --reload
```
The API will be available at: `http://127.0.0.1:8000`

### 2️⃣ Run the Streamlit Frontend
```sh
streamlit run frontend/app.py
```

## API Endpoints
| Endpoint           | Method | Description |
|-------------------|--------|-------------|
| `/`               | GET    | Check if API is running |
| `/query/`         | GET    | Process user queries (text & visualization) |
| `/summary/`       | GET    | Get dataset summary (passengers, survival rate, etc.) |

## Example Queries
- **Text-based:**
  - "What is the average age of passengers?"
  - "Tell me about survival by class."
- **Graph-based:**
  - "Show me the age distribution."
  - "What is the fare trend?"
  - "Pie chart of passenger class distribution."

## Technologies Used
- **Python** 🐍
- **FastAPI** ⚡ (Backend API)
- **Streamlit** 📺 (Frontend UI)
- **Google Gemini AI** 🤖 (Query Processing)
- **Matplotlib & Seaborn** 📊 (Data Visualization)
- **Pandas** 📝 (Data Handling)

## Screenshots
📌Asking questions related to Titanic :
 ![image](https://github.com/user-attachments/assets/c8b3ce91-d583-4991-8d9d-639c58b1c870)

📌Pie Chart :
![image](https://github.com/user-attachments/assets/4a678c11-9e3e-46e6-8c85-e06b32328cc2)



## Future Enhancements
- ✅ Improve AI response accuracy
- ✅ Add more visualization options
- ✅ Deploy on a cloud server (AWS, GCP, etc.)

## License
📜 This project is open-source and available under the MIT License.

🤝 Contributions are welcome! Feel free to fork the repository and submit a pull request.

🚀 **Happy Coding!** 🎯

