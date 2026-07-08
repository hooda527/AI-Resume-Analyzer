import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def load_gemini_model():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Please create a .env file and add your API key."
        )

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    return model


def analyze_resume(prompt):
    try:
        model = load_gemini_model()

        response = model.generate_content(prompt)

        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        text = response.text.strip()

        # Remove markdown JSON formatting
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        # Convert response into Python dictionary
        result = json.loads(text)

        return result

    except json.JSONDecodeError:
        raise ValueError(
            "Gemini response is not valid JSON. Please check your prompt format."
        )

    except Exception as e:
        raise Exception(f"Gemini API Error: {str(e)}")