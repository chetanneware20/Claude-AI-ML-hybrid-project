import google.generativeai as genai
import streamlit as st

def medical_chat(user_question):

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are a helpful medical assistant.
    Answer the question in simple language.
    Always recommend consulting a doctor.

    Question:
    {user_question}
    """

    response = model.generate_content(prompt)

    return response.text
