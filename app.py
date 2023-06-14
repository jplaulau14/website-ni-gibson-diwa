import os
import streamlit as st
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from environment variable
key = os.getenv('API_KEY')

# Set the OpenAI API key
openai.api_key = key

st.set_page_config(page_title="Website ni Gibson Marshall Diwa")

# Create a Streamlit interface
st.title("Chat with AI")

# Get the user input
user_input = st.text_input("You: ")

if st.button("Send"):
    # Initialize the messages with a system message
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": user_input,
        }
    ]

    # Make an API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
    )

    # Get the assistant's message
    assistant_message = response.choices[0].message.content

    # Display the assistant's message
    st.write(f"AI: {assistant_message}")
