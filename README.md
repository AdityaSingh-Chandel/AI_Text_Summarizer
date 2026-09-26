# AI Text Summarizer

An AI-powered text summarization application built with **Python, Streamlit, and the Gemini API**. The application allows users to generate summaries in different formats based on their requirements.

---

## ✨ Features

* Generate **concise summaries**
* Generate **detailed summaries**
* Generate **bullet-point summaries**
* Simple and user-friendly **Streamlit interface**
* AI-powered text processing using the **Gemini API**

---

## 🛠️ Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Application development         |
| Streamlit     | Web interface                   |
| Gemini API    | AI-powered text summarization   |
| python-dotenv | Environment variable management |

---

## 📋 Prerequisites

Make sure the following are installed on your system:

* **Python 3.x**
* **Git**
* **Command Prompt (CMD)** or another terminal

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```cmd
git clone <repository-url>
```

### 2. Navigate to the Project Directory

```cmd
cd "<document-directory>\AI_Text_Summarizer"
```

> Replace `<document-directory>` with the location where you cloned the repository.

### 3. Activate the Virtual Environment

For **Windows CMD**:

```cmd
venv\Scripts\activate
```

After activation, you should see `(venv)` at the beginning of your terminal prompt.

### 4. Install Dependencies

```cmd
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> Replace `your_api_key_here` with your actual Gemini API key.
> **Do not commit or upload your `.env` file to GitHub.**

### 6. Run the Application

```cmd
python -m streamlit run app.py
```

The application will start locally and automatically open in your default web browser.

---

## 📁 Project Structure

```text
AI_Text_Summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
├── .env
├── .gitignore
├── venv/
└── README.md
```

---

## 📌 Notes

* Ensure your **Gemini API key** is correctly configured before running the application.
* Keep your `.env` file private and never upload API keys or other secrets to GitHub.
* Activate the virtual environment before running the application.
