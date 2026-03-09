import google.generativeai as genai

def medical_chat(user_input, api_key):

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Load Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Prompt for healthcare chatbot
    prompt = f"""
    You are a helpful healthcare AI assistant.

    Provide general medical information based on the user's question.
    Do not give final medical diagnosis.
    Always recommend consulting a qualified doctor for serious issues.

    User Question:
    {user_input}
    """

    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text
        else:
            return "Sorry, I couldn't generate a response."

    except Exception as e:
        return f"Error: {str(e)}"
