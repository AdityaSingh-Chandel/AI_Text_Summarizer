import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def summarize_text(text):

    prompt = f"""
    You are a professional summarizer.

    Analyze the text and provide:

    1. Short Summary (3-4 lines)
    2. Detailed Summary
    3. Key Bullet Points

    Text:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text