# 📘 Emotion Detection Web App using Watson NLP

This is the final project for the “Developing AI Applications with Python and Flask” course, where we build an Emotion Detection web application using IBM Watson’s NLP service and Flask.

The application identifies emotions such as **joy**, **anger**, **sadness**, **fear**, and **disgust** from any given English text input. The output includes the score for each emotion and identifies the **dominant emotion** in the statement.

---

## 📌 Project Overview

Emotion detection is a more advanced form of sentiment analysis that extracts nuanced emotional context from text. This technology is used widely in recommendation engines, social media monitoring, customer feedback analysis, and intelligent chatbots.

---

## ✅ Project Tasks

| Task No. | Description |
|----------|-------------|
| **Task 1** | **Fork and Clone** the IBM GitHub repository. |
| **Task 2** | **Build an emotion detection function** using the Watson NLP API. |
| **Task 3** | **Format the output** to return scores for 5 emotions and the dominant one. |
| **Task 4** | **Package the project** with structured Python modules and folders. |
| **Task 5** | **Write and run unit tests** for the `emotion_detector()` function. |
| **Task 6** | **Deploy the application using Flask** with a simple HTML interface. |
| **Task 7** | **Handle errors** and invalid input gracefully. |
| **Task 8** | **Run static code analysis** (e.g., using `pylint`) and improve code quality. |

---

## 🚀 Features

- Emotion analysis of natural language input  
- Scores for: `joy`, `anger`, `fear`, `sadness`, `disgust`  
- Returns the **dominant emotion**  
- Flask-based web UI  
- Error handling for invalid/empty input  
- Unit tested & statically analyzed Python code  

---

## 🔧 Installation & Usage

### 🔁 Clone the Repository

```bash
git clone https://github.com/vanshika2608/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

### 🐍 Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 🚀 Run the Flask App

```bash
python server.py
```

Then open your browser and go to:  
`http://127.0.0.1:5000/`

---

## 🧪 Run Unit Tests

```bash
python -m unittest discover tests
```

---

## 📊 Run Static Code Analysis

```bash
pylint EmotionDetection/*.py server.py
```

Aim for a score as close to **10/10** as possible.

---

## 📸 Screenshots
<img width="948" alt="6b_deployment_test" src="https://github.com/user-attachments/assets/e3b1fd52-a726-4e98-9ed7-1e7030509a91" />
<img width="902" alt="7c_error_handling_interface" src="https://github.com/user-attachments/assets/91a48dfd-8051-488c-8416-e7ba3fb96365" />
<img width="536" alt="8b_static_code_analysis" src="https://github.com/user-attachments/assets/65dc955c-0847-4576-8a9a-cd3e43b856da" />


## 🙌 Acknowledgments

- IBM Skills Network  
- Watson NLP API  
- Flask  
- Python Unittest Framework  

---

## 📬 Contact

Created by **[Vanshika](https://github.com/vanshika2608)**  
For academic purposes as part of the IBM Developer Skills Network course.
