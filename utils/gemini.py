import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def load_gemini_model():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Please create a .env file and add your own API key."
        )

    genai.configure(api_key=api_key)

    return genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(prompt):

    model = load_gemini_model()

    response = model.generate_content(prompt)

    return response.text