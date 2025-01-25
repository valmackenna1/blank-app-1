import openai
import streamlit as st
import os

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Title and Instructions
st.title("Custom GPT-Powered Chat")
st.write("Chat with our custom AI assistant tailored for your needs.")

# User Input
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    try:
        # Send input to custom GPT
        response = openai.ChatCompletion.create(
            model="67684b5d111c8191b20b1a68e585aa5d-lenny-lungman",  # Replace with your custom GPT model ID
            messages=[{"role": "user", "content": user_input}],
        )
        # Display response
        st.write("AI:", response['choices'][0]['message']['content'])
    except Exception as e:
        st.error(f"Error: {e}")