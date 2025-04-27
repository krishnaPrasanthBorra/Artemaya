import streamlit as st
import os
import time
import random
from dotenv import load_dotenv
import google.generativeai as genai
from utilities import check_api_key_validity, save_conversation, log_performance

# Load environment variables
load_dotenv()

# Configure API Keys
GOOGLE_API_KEYS = []
for i in range(1, 6):  # Assuming up to 5 keys
    key_name = f"GOOGLE_API_KEY_{i}"
    if os.getenv(key_name):
        api_key = os.getenv(key_name)
        if check_api_key_validity(api_key):
            GOOGLE_API_KEYS.append(api_key)

if not GOOGLE_API_KEYS:
    st.error("No API keys found. Please set them in .env file.")
    st.stop()

# Initialize session state for API key management
if "api_key_index" not in st.session_state:
    st.session_state.api_key_index = 0
if "key_cooldowns" not in st.session_state:
    st.session_state.key_cooldowns = {key: 0 for key in GOOGLE_API_KEYS}

# App configuration
st.set_page_config(page_title="Artemaya", page_icon="🌟", layout="wide")

# Load CSS
def load_css():
    with open("style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to get the next available API key
def get_api_key():
    current_time = time.time()
    # Reset cooldowns for keys that have waited long enough
    for key, cooldown_time in st.session_state.key_cooldowns.items():
        if current_time > cooldown_time:
            st.session_state.key_cooldowns[key] = 0
    
    # Find keys not on cooldown
    available_keys = [key for key, cooldown in st.session_state.key_cooldowns.items() if cooldown == 0]
    
    if available_keys:
        return random.choice(available_keys)
    else:
        # If all keys are on cooldown, use the one with the shortest remaining cooldown
        return min(st.session_state.key_cooldowns, key=st.session_state.key_cooldowns.get)

# Function to mark a key as being on cooldown (e.g., after an error)
def set_key_cooldown(key, seconds=60):
    st.session_state.key_cooldowns[key] = time.time() + seconds

# Function to get AI response
def get_ai_response(prompt, history=None):
    api_key = get_api_key()
    start_time = time.time()
    
    try:
        # Configure the API
        genai.configure(api_key=api_key)
        
        # Set up model configuration
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 2048,
        }
        
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
        
        # Initialize the model
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        
        # Format conversation history
        if history:
            chat = model.start_chat(history=history)
            response = chat.send_message(prompt)
        else:
            response = model.generate_content(prompt)
        
        end_time = time.time()
        log_performance("get_ai_response", start_time, end_time, "success", 
                       {"prompt_length": len(prompt), "response_length": len(response.text)})
        
        return response.text
    
    except Exception as e:
        # Set a cooldown for this key if there was an error
        set_key_cooldown(api_key)
        
        end_time = time.time()
        log_performance("get_ai_response", start_time, end_time, "failure", 
                       {"error": str(e)})
        
        # Return error message
        error_msg = str(e)
        if "quota" in error_msg.lower():
            return "I'm currently experiencing high traffic. Please try again in a moment."
        elif "invalid" in error_msg.lower() and "key" in error_msg.lower():
            return "API configuration issue. Please check your setup."
        else:
            return f"I encountered an error. Please try again or reformulate your question."

# Format conversation history for the AI model
def format_chat_history(messages):
    history = []
    for msg in messages:
        if msg["role"] == "user":
            role = "user"
        else:
            role = "model"
        history.append({"role": role, "parts": [msg["content"]]})
    return history

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
    
    # Add a sidebar with options
    with st.sidebar:
        st.header("Options")
        if st.button("Clear Conversation"):
            st.session_state.messages = []
            st.rerun()
        
        # Add a save conversation button
        if st.session_state.messages and st.button("Save Conversation"):
            if save_conversation(st.session_state.messages):
                st.success("Conversation saved successfully!")
            else:
                st.error("Failed to save conversation.")
    
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
        
        # Display assistant response (with a loading spinner)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Format the conversation history for the AI model
                if len(st.session_state.messages) > 1:
                    history = format_chat_history(st.session_state.messages[:-1])
                    response = get_ai_response(prompt, history)
                else:
                    response = get_ai_response(prompt)
                
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Footer
    st.markdown("<div class='footer'>Artemaya - Created by Krishna Prasanth Borra</div>", 
               unsafe_allow_html=True)

if __name__ == "__main__":
    main() 