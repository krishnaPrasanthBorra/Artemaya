import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from datetime import datetime
import numpy as np
from PIL import Image
from utils import enhance_response_with_knowledge
import random

# Load environment variables
load_dotenv()

# Configure API key - simplified to use just one key
api_key = "AIzaSyAHXyr8yF6KaGCvEBxnJdcaKINS6kAuNJE"  # Using the user's new API key
genai.configure(api_key=api_key)

# Check if Gemini API is accessible
try:
    print(f"Using API key: {api_key}")
    test_model = genai.GenerativeModel('gemini-1.5-pro')
    _ = test_model.generate_content("Hello")
    print(f"API connection successful!")
except Exception as e:
    print(f"WARNING: Error connecting to Gemini API: {str(e)}")
    print("The application will start, but chat functionality may be limited.")
    print("Please ensure your API key is correct and has access to the Gemini model.")

# Set page configuration
st.set_page_config(
    page_title="ASHA - Your Career Companion",
    page_icon="👩‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #FF4B91;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #444;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-container {
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
    }
    .user-bubble {
        background-color: #FF4B91;
        color: white;
        border-radius: 18px 18px 0 18px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 80%;
        align-self: flex-end;
        display: inline-block;
        margin-left: auto;
    }
    .bot-bubble {
        background-color: #F5F5F5;
        color: #333;
        border-radius: 18px 18px 18px 0;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 80%;
        align-self: flex-start;
        display: inline-block;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
    }
    .send-button {
        border-radius: 20px;
        background-color: #FF4B91;
        color: white;
    }
    .css-18e3th9 {
        padding-top: 0;
    }
    .css-1d391kg {
        padding-top: 1rem;
    }
    .career-stage-button {
        background-color: #FF4B91;
        color: white;
        border-radius: 20px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        margin: 5px;
        transition: all 0.3s;
    }
    .career-stage-button:hover {
        background-color: #FF6BA9;
        transform: scale(1.05);
    }
    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'career_stage' not in st.session_state:
    st.session_state.career_stage = None

if 'is_woman' not in st.session_state:
    st.session_state.is_woman = None

if 'showing_welcome' not in st.session_state:
    st.session_state.showing_welcome = True

if 'user_context' not in st.session_state:
    st.session_state.user_context = {
        "career_goals": None,
        "industry": None,
        "skills": [],
        "challenges": []
    }

if 'stage_selection' not in st.session_state:
    st.session_state.stage_selection = False
    
# Add response caching to reduce API calls
if 'response_cache' not in st.session_state:
    st.session_state.response_cache = {}
    st.session_state.cache_hits = 0
    st.session_state.cache_misses = 0
    # Maximum cache size
    st.session_state.max_cache_size = 50
    
# Track API usage
if 'api_calls' not in st.session_state:
    st.session_state.api_calls = 0

# Helper functions for the chatbot
def get_system_prompt(user_input=None):
    """Generate a comprehensive system prompt that includes all guidance and context detection"""
    # Career stage context
    career_stage_context = ""
    if st.session_state.career_stage == "Starter":
        career_stage_context = """
        This user is just starting their career. Focus on entry-level opportunities, 
        foundational skill development, networking tips for beginners, and first job strategies.
        Provide resources suitable for someone with limited professional experience.
        """
    elif st.session_state.career_stage == "Restarter":
        career_stage_context = """
        This user is returning to work after a career break. Focus on rebuilding confidence,
        updating skills, addressing resume gaps positively, and navigating the changed job market.
        Offer strategies for explaining career breaks constructively.
        """
    elif st.session_state.career_stage == "Riser":
        career_stage_context = """
        This user is advancing in their established career. Focus on leadership development,
        advanced skills, negotiation strategies, professional brand building, and mentorship.
        Provide resources for someone looking to move to the next level in their career.
        """
    
    # Current user context
    user_context_str = f"""
    Career Goals: {st.session_state.user_context['career_goals'] or 'Not specified yet'}
    Industry: {st.session_state.user_context['industry'] or 'Not specified yet'}
    Skills: {', '.join(st.session_state.user_context['skills']) if st.session_state.user_context['skills'] else 'Not specified yet'}
    Challenges: {', '.join(st.session_state.user_context['challenges']) if st.session_state.user_context['challenges'] else 'Not specified yet'}
    """
    
    # Add real-time context extraction instructions
    context_extraction = ""
    if user_input:
        context_extraction = f"""
        IMPORTANT: When responding, extract and use any relevant context from the user's current message:
        Current message: "{user_input}"
        
        Context extraction guidelines:
        1. If they mention career goals, use this to inform your response
        2. If they mention an industry, provide industry-specific guidance
        3. If they mention skills, acknowledge and build upon these
        4. If they mention challenges, address these directly
        5. Look for career stage indicators (starter, returning, advancing) and adjust accordingly
        """
    
    # Career relevance guidance
    career_relevance = """
    Important: Only respond to career-related questions. 
    If the user asks about non-career topics, politely redirect them with:
    "I'm here specifically to help with your career growth. Could we focus on how I can support your professional journey? Feel free to ask me about job opportunities, skill development, interview preparation, or any other career-related topics."
    """
    
    # Add gender guidance
    gender_guidance = """
    You are specifically designed to support women in their careers. If you detect the user is not a woman, respond with:
    "ASHA is specifically designed to support women in their career journeys. However, I'd be happy to recommend other career resources that might better suit your needs."
    Look for explicit gender indicators before making this determination.
    """
    
    # Complete system prompt
    system_prompt = f"""
    You are ASHA, an AI-powered career companion specifically designed to empower women in their careers.
    Your responses should be warm, empathetic, and inspirational while remaining practical and actionable.
    
    Core Guidelines:
    1. Always maintain a supportive, empathetic tone that empowers women.
    2. Provide specific, actionable career advice rather than general platitudes.
    3. Keep responses conversational, as if coming from a trusted mentor.
    4. Use storytelling techniques when appropriate to inspire and create emotional connection.
    5. Focus ONLY on career-related topics and gently redirect non-career conversations.
    6. Never reinforce gender stereotypes or biases.
    7. Do not store, request or share sensitive personal data.
    8. Avoid making personal opinions or predictions.
    9. Be inclusive and sensitive to diverse backgrounds and circumstances.
    10. Remember you are a career companion, not a general assistant.
    
    {career_relevance}
    
    {gender_guidance}
    
    USER CONTEXT:
    Career Stage: {st.session_state.career_stage or 'Not determined yet'}
    {career_stage_context}
    
    User Details:
    {user_context_str}
    
    {context_extraction}
    
    For career advice, include:
    - Specific actionable steps
    - Relevant resources or communities when appropriate
    - Empowering language that builds confidence
    """
    
    return system_prompt

def get_gemini_response(user_input):
    """Get response from Gemini model with the appropriate context - now with all features in one call"""
    system_prompt = get_system_prompt(user_input)
    
    # Generate a cache key based on user input and career stage
    cache_key = f"{user_input}_{st.session_state.career_stage}"
    
    # Check if we have a cached response
    if cache_key in st.session_state.response_cache:
        st.session_state.cache_hits += 1
        return st.session_state.response_cache[cache_key]
    
    # Track cache miss
    st.session_state.cache_misses += 1
    
    # Format messages for the model
    conversation_history = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        conversation_history.append({"role": role, "parts": [msg["content"]]})
    
    # Track API calls
    st.session_state.api_calls += 1
    
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Start a chat session
        chat = model.start_chat(history=conversation_history)
        
        # Generate response
        response = chat.send_message(
            [system_prompt, user_input],
        )
        
        # Enhance the response with domain-specific knowledge
        enhanced_response = enhance_response_with_knowledge(
            user_input, 
            st.session_state.career_stage,
            response.text
        )
        
        # Cache the response
        if len(st.session_state.response_cache) >= st.session_state.max_cache_size:
            # Remove a random item if cache is full
            keys = list(st.session_state.response_cache.keys())
            if keys:
                del st.session_state.response_cache[random.choice(keys)]
        
        # Add to cache
        st.session_state.response_cache[cache_key] = enhanced_response
        
        return enhanced_response
    
    except Exception as e:
        error_msg = str(e).lower()
        
        # Provide specific error messages
        if "quota" in error_msg or "rate limit" in error_msg:
            return "I've reached my usage limit. Please try again later."
        elif "not available" in error_msg or "unavailable" in error_msg:
            return ("The Gemini model is currently unavailable. This could be due to high demand. "
                   "Please try again in a few minutes.")
        else:
            return f"I apologize, but I'm having trouble connecting right now. Error: {str(e)}"

def extract_and_update_context(user_input, bot_response):
    """Extract and update user context from the conversation without making API calls"""
    # Look for career stage indicators in user input
    lower_input = user_input.lower()
    
    # Simple keyword-based extraction
    # Career stage detection
    if not st.session_state.career_stage:
        starter_keywords = ["starting", "beginner", "entry level", "new graduate", "first job", "student"]
        restarter_keywords = ["returning", "break", "gap", "maternity", "re-enter", "restart"]
        riser_keywords = ["promotion", "advancing", "leadership", "senior", "manager", "director", "experienced"]
        
        if any(keyword in lower_input for keyword in starter_keywords):
            st.session_state.career_stage = "Starter"
        elif any(keyword in lower_input for keyword in restarter_keywords):
            st.session_state.career_stage = "Restarter"
        elif any(keyword in lower_input for keyword in riser_keywords):
            st.session_state.career_stage = "Riser"
    
    # Industry detection
    industry_keywords = {
        "technology": ["tech", "software", "it", "developer", "programming", "digital"],
        "healthcare": ["health", "medical", "nurse", "doctor", "hospital", "pharma"],
        "finance": ["finance", "banking", "accounting", "investment", "financial"],
        "education": ["education", "teaching", "teacher", "school", "academic", "professor"],
        "creative": ["design", "art", "writing", "creative", "media"]
    }
    
    for industry, keywords in industry_keywords.items():
        if any(keyword in lower_input for keyword in keywords) and not st.session_state.user_context["industry"]:
            st.session_state.user_context["industry"] = industry
            break
    
    # Skills extraction - look for common career skills
    skill_keywords = ["experience in", "skilled in", "knowledge of", "proficient in", "expert in", "familiar with"]
    for phrase in skill_keywords:
        if phrase in lower_input:
            # Extract the skill mentioned after the phrase
            index = lower_input.find(phrase) + len(phrase)
            skill_text = user_input[index:].strip()
            # Take up to the next punctuation or end of string
            for i, char in enumerate(skill_text):
                if char in ".,;!?":
                    skill_text = skill_text[:i]
                    break
            
            if skill_text and len(skill_text) > 2 and skill_text not in st.session_state.user_context["skills"]:
                st.session_state.user_context["skills"].append(skill_text)
    
    # Challenge extraction
    challenge_keywords = ["struggle with", "challenge", "difficult", "problem", "issue", "hard time with"]
    for phrase in challenge_keywords:
        if phrase in lower_input:
            # Extract the challenge mentioned after the phrase
            index = lower_input.find(phrase) + len(phrase)
            challenge_text = user_input[index:].strip()
            # Take up to the next punctuation or end of string
            for i, char in enumerate(challenge_text):
                if char in ".,;!?":
                    challenge_text = challenge_text[:i]
                    break
            
            if challenge_text and len(challenge_text) > 2 and challenge_text not in st.session_state.user_context["challenges"]:
                st.session_state.user_context["challenges"].append(challenge_text)
    
    # Career goals extraction
    goal_keywords = ["goal", "aim", "objective", "aspire", "want to", "hope to", "plan to"]
    for phrase in goal_keywords:
        if phrase in lower_input:
            # Extract the goal mentioned after the phrase
            index = lower_input.find(phrase) + len(phrase)
            goal_text = user_input[index:].strip()
            # Take up to the next punctuation or end of string
            for i, char in enumerate(goal_text):
                if char in ".,;!?":
                    goal_text = goal_text[:i]
                    break
            
            if goal_text and len(goal_text) > 5:
                st.session_state.user_context["career_goals"] = goal_text

def set_career_stage(stage):
    """Set the user's career stage explicitly"""
    st.session_state.career_stage = stage
    st.session_state.stage_selection = False
    
    # Add a message from ASHA acknowledging the stage selection
    stage_messages = {
        "Starter": "Thanks for letting me know you're just starting your career journey! I'll tailor my guidance to help you build a strong foundation. What specific aspect of starting your career would you like help with?",
        "Restarter": "I understand you're returning to work after a break. That takes courage! I'll focus on helping you leverage your previous experience while navigating this transition. What's your biggest concern about restarting your career?",
        "Riser": "Great to know you're looking to advance in your established career! I'll focus on strategies to help you continue growing professionally. What specific aspect of career advancement are you currently focusing on?"
    }
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": stage_messages[stage]
    })

# Main application interface
def main():
    # Header
    st.markdown('<h1 class="main-header">ASHA</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your AI Career Companion</p>', unsafe_allow_html=True)
    
    # Welcome message
    if st.session_state.showing_welcome:
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.info("""
                👋 Welcome to ASHA! I'm your AI career companion dedicated to empowering women in their professional journeys.
                
                I can help with:
                - Career guidance and planning
                - Resume and interview preparation
                - Skill development recommendations
                - Work-life balance strategies
                - Navigating workplace challenges
                
                Tell me a bit about your career situation so I can provide personalized guidance!
                """)
                
                if st.button("Get Started"):
                    st.session_state.showing_welcome = False
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Hi there! I'm ASHA, your AI career companion. I'm here to help you navigate your professional journey with personalized guidance. Could you tell me a bit about your current career situation? Are you just starting out, returning after a break, or looking to advance in your established career?"
                    })
                    st.rerun()
    
    # Career stage selection screen
    elif st.session_state.stage_selection:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>To personalize my guidance, please select your career stage:</h3>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                st.markdown("""
                <div style='display: flex; justify-content: space-around; margin: 2rem 0;'>
                    <button class='career-stage-button' id='starter-btn' onclick='selectStage("Starter")'>Just Starting</button>
                    <button class='career-stage-button' id='restarter-btn' onclick='selectStage("Restarter")'>Returning After a Break</button>
                    <button class='career-stage-button' id='riser-btn' onclick='selectStage("Riser")'>Advancing My Career</button>
                </div>
                
                <script>
                function selectStage(stage) {
                    const selectEvent = new CustomEvent('selectStage', { detail: { stage: stage } });
                    window.parent.document.dispatchEvent(selectEvent);
                }
                </script>
                """, unsafe_allow_html=True)
                
                # Since JavaScript can't directly interact with Streamlit, use buttons
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("Just Starting", key="starter_btn"):
                        set_career_stage("Starter")
                
                with col2:
                    if st.button("Returning After a Break", key="restarter_btn"):
                        set_career_stage("Restarter")
                
                with col3:
                    if st.button("Advancing My Career", key="riser_btn"):
                        set_career_stage("Riser")
    
    # Chat container
    else:
        chat_container = st.container()
        with chat_container:
            # Display chat messages
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f'<div style="text-align: right;"><div class="user-bubble">{message["content"]}</div></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="text-align: left;"><div class="bot-bubble">{message["content"]}</div></div>', unsafe_allow_html=True)
        
        # User input
        with st.container():
            col1, col2 = st.columns([6, 1])
            with col1:
                user_input = st.text_input("Type your message here...", key="user_input", label_visibility="collapsed")
            with col2:
                send_button = st.button("Send", use_container_width=True)
            
            if send_button and user_input:
                # Add user message to chat
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_input
                })
                
                # Check if we should prompt for career stage selection
                if not st.session_state.career_stage and len(st.session_state.messages) >= 3:
                    words = user_input.lower().split()
                    career_keywords = ["career", "job", "work", "professional", "position", "role"]
                    
                    # If they've mentioned career-related terms, offer explicit selection
                    if any(word in career_keywords for word in words):
                        st.session_state.stage_selection = True
                        st.rerun()
                        return
                
                # Generate response - now handling all context extraction and detection in one API call
                response = get_gemini_response(user_input)
                
                # Extract and update context from the conversation
                extract_and_update_context(user_input, response)
                
                # Add bot response to chat
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                
                # Rerun to update the UI
                st.rerun()
    
    # Debug section (hidden in sidebar for development)
    with st.sidebar:
        st.title("ASHA Career Companion")
        
        # Career stage manual selection
        if not st.session_state.stage_selection and st.session_state.career_stage is None:
            if st.button("Set Career Stage"):
                st.session_state.stage_selection = True
                st.rerun()
        
        if st.checkbox("Show Debug Info"):
            st.subheader("Session State")
            st.write(f"Career Stage: {st.session_state.career_stage}")
            st.write(f"Is Woman: {st.session_state.is_woman}")
            
            st.subheader("User Context")
            st.json(st.session_state.user_context)
            
            st.subheader("API Usage")
            st.write(f"Total API Calls: {st.session_state.api_calls}")
            st.write(f"Active API Key: {api_key}")
            
            st.subheader("Cache Performance")
            total_requests = st.session_state.cache_hits + st.session_state.cache_misses
            hit_rate = (st.session_state.cache_hits / total_requests * 100) if total_requests > 0 else 0
            st.write(f"Cache Hit Rate: {hit_rate:.1f}%")
            st.write(f"Cache Size: {len(st.session_state.response_cache)} / {st.session_state.max_cache_size}")
        
        if st.button("Reset Chat"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main() 