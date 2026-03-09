import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(
    page_title="Healthcare AI Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Healthcare AI Assistant")
st.write("AI-powered medical chatbot using Google Gemini")

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Ask a medical question")

if st.button("Ask AI"):

    if user_input.strip() != "":

        prompt = f"""
        You are a professional healthcare AI assistant.

        Provide general medical information.
        Do not give a final diagnosis.
        Always suggest consulting a qualified doctor.

        Question: {user_input}
        """

        try:
            response = model.generate_content(prompt)

            # Safe response handling
            if response and hasattr(response, "text"):
                ai_response = response.text
            else:
                ai_response = "⚠️ AI could not generate a response."

            st.session_state.chat_history.append(("User", user_input))
            st.session_state.chat_history.append(("AI", ai_response))

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Display chat history
st.subheader("💬 Chat History")

for role, text in st.session_state.chat_history:

    if role == "User":
        st.markdown(f"**👤 You:** {text}")
    else:
        st.markdown(f"**🤖 AI:** {text}")
