import anthropic
import streamlit as st

def medical_chat(user_question):

    client = anthropic.Anthropic(
        api_key=st.secrets["CLAUDE_API_KEY"]
    )

    prompt = f"""
    You are a helpful healthcare assistant.

    Provide safe medical information but always include a disclaimer
    that the user should consult a doctor.

    Question:
    {user_question}
    """

    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text
