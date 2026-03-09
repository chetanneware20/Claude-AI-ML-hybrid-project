import google.generativeai as genai
import streamlit as st

def medical_chat(user_question):

    if "GEMINI_API_KEY" not in st.secrets:
        return "⚠️ Gemini API key not configured."

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are a helpful medical assistant.

    Answer health questions in simple language.
    Always recommend consulting a doctor.

    Question:
    {user_question}
    """

    response = model.generate_content(prompt)

    return response.text
