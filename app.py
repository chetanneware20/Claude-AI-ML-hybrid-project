import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(
    page_title="Healthcare AI Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Healthcare AI Assistant")
st.write("AI powered medical chatbot using Google Gemini")

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Ask a medical question")

if st.button("Ask AI"):

    if user_input:

        prompt = f"""
        You are a healthcare assistant.
        Provide helpful medical information but remind users to consult a doctor.

        Question: {user_input}
        """

        try:
            response = model.generate_content(prompt)

            st.session_state.chat_history.append(("User", user_input))
            st.session_state.chat_history.append(("AI", response.text))

        except Exception as e:
            st.error(e)

# Display chat
for role, text in st.session_state.chat_history:

    if role == "User":
        st.markdown(f"**👤 You:** {text}")
    else:
        st.markdown(f"**🤖 AI:** {text}")
