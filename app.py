import streamlit as st
from chatbot import medical_chat

st.set_page_config(page_title="AI Medical Chatbot")

st.title("🏥 AI Medical Chatbot")
st.write("Ask health related questions")

user_input = st.text_input("Enter your symptoms or question")

if st.button("Ask AI"):

    if user_input != "":

        with st.spinner("AI is thinking..."):

            response = medical_chat(user_input)

        st.subheader("🤖 AI Response")
        st.write(response)
