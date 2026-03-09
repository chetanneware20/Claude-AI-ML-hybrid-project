import google.generativeai as genai

def medical_chat(user_input, api_key):

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Use supported model
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    prompt = f"""
    You are a helpful healthcare AI assistant.

    Provide general medical information.
    Do not give final diagnosis.
    Suggest consulting a doctor for serious conditions.

    User Question:
    {user_input}
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
