import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API Key
GOOGLE_API_KEYS = []
for i in range(1, 6):  # Assuming up to 5 keys
    key_name = f"GOOGLE_API_KEY_{i}"
    if os.getenv(key_name):
        GOOGLE_API_KEYS.append(os.getenv(key_name))

if not GOOGLE_API_KEYS:
    st.error("No API keys found. Please set them in .env file.")
    st.stop()

# App configuration
st.set_page_config(page_title="Artemaya", page_icon="🌟", layout="wide")

# Load CSS
def load_css():
    with open("style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Define the app
def main():
    # Load custom CSS
    load_css()
    
    # App header
    st.markdown("<h1 class='main-header'>Artemaya</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Your AI Assistant</h3>", unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages in a container
    with st.container():
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"<div class='user-message'>{message['content']}</div>", 
                           unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='assistant-message'>{message['content']}</div>", 
                           unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Get user input
    if prompt := st.chat_input("How can I help you today?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            response = "This is a placeholder response. Implement actual AI response here."
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Footer
    st.markdown("<div class='footer'>Artemaya - Created by Krishna Prasanth Borra</div>", 
               unsafe_allow_html=True)

if __name__ == "__main__":
    main() 