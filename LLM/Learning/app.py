import streamlit as st
import google.generativeai as gai
from dotenv import load_dotenv
import os

# Environment variables load karna
load_dotenv()
API_KEY = os.getenv("GEN_API_KEY")

# Google Gemini AI configure karna
gai.configure(api_key=API_KEY)
model = gai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit UI setup
st.title("AI Chatbot")
st.write("Ask any question and AI will answer it.")

# User se input lena
user_question = st.text_input("whats your question?")

# Jab user submit kare to AI ko bhejna
if st.button("Submit"):
    if user_question.strip():  # Empty input handle karna
        # yani khali input ay to else chaly wrna token  zaya hongy
        response = model.generate_content(user_question)
        # quation bheja ai ko 
        st.subheader("AI Answer:")
        # ai ka answer display karna
        st.write(response.text.strip())
        # strip function se extra spaces remove karna
    else:
        st.warning("Please enter a question to get an answer.")
