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

## 📸 Screenshot Requirements

Please ensure the following screenshots are taken and saved:

| Screenshot Name | Description |
|-----------------|-------------|
| `<img width="372" alt="1_folder_structure" src="https://github.com/user-attachments/assets/95900a2c-60c5-4a17-b63c-bd88a5ed550e" />` | After forking the original repo |
| `<img width="831" alt="2a_emotion_detection" src="https://github.com/user-attachments/assets/aa9e13c8-fa80-40eb-8660-2aed9db58d8f" />``<img width="605" alt="2b_application_creation" src="https://github.com/user-attachments/assets/d2f9924e-a0d0-4ad6-b03f-9d5000762717" />` | Emotion detection API response |
| `<img width="665" alt="3a_output_formatting" src="https://github.com/user-attachments/assets/59d2722f-c6f1-4604-922f-a30cd579222f" />``<img width="674" alt="3b_formatted_output_test" src="https://github.com/user-attachments/assets/f62f0093-95c3-40b8-9a9a-1ef795da5a33" />`| Console output showing formatted scores |
| `<img width="699" alt="4a_packaging" src="https://github.com/user-attachments/assets/2ba4b1c6-1898-4333-ae07-c40d635cdd68" />``<img width="566" alt="4b_packaging_test" src="https://github.com/user-attachments/assets/bd8419cd-90a2-4bd3-9be5-bd456d5f1522" />` | Folder structure after packaging |
| `<img width="699" alt="5a_unit_testing" src="https://github.com/user-attachments/assets/8bbc1c40-9007-484b-a422-9b76c54048c4" />``<img width="747" alt="5b_unit_testing_result" src="https://github.com/user-attachments/assets/f9901238-6ca0-4194-b5ea-17fa0faba054" />` | Running unit tests and results |
| `<img width="948" alt="6b_deployment_test" src="https://github.com/user-attachments/assets/833bd16d-9fcb-48ae-bb37-a112071979f0" />` | UI of the Flask app with response |
| `<img width="902" alt="7c_error_handling_interface" src="https://github.com/user-attachments/assets/75cb39e5-259f-4600-85cd-de8491122548" />` | Message when invalid input is given |
| `<img width="536" alt="8b_static_code_analysis" src="https://github.com/user-attachments/assets/823eaf13-b09c-4241-b12a-d860fd0f879b" />` | Static code score (preferably > 9) |

---

## 🙌 Acknowledgments

- IBM Skills Network  
- Watson NLP API  
- Flask  
- Python Unittest Framework  

---

## 📬 Contact

Created by **[Vanshika](https://github.com/vanshika2608)**  
For academic purposes as part of the IBM Developer Skills Network course.
