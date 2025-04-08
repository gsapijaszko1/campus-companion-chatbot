# campus_companion_chatbot_ai.py

import streamlit as st
import openai
import os

# --- Page Setup ---
st.set_page_config(page_title="AI Campus Companion Chatbot")
st.title("🤖 AI-Powered Campus Companion Chatbot")
st.write("Ask me anything about college life — I'm powered by GPT!")

# --- OpenAI API Key Input (Colab compatible) ---
openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")

# --- User Question Input ---
user_question = st.text_input("Type your question here:")

# --- GPT-based Response ---
def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful college assistant that answers questions about student life, deadlines, resources, and more."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# --- Generate and Display Response ---
if user_question and openai_api_key:
    openai.api_key = openai_api_key
    with st.spinner("Thinking..."):
        response = get_ai_response(user_question)
    st.markdown(f"**You asked:** {user_question}")
    st.markdown(f"**Chatbot says:** {response}")

elif user_question and not openai_api_key:
    st.warning("Please enter your OpenAI API key to get a response.")
