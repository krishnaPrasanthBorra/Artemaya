"""
Utility functions for the Artemaya application.
"""

import os
import time
import random
import json
from datetime import datetime

# API Key Management Functions
def check_api_key_validity(api_key):
    """
    Checks if an API key is properly formatted.
    This is a basic check and doesn't validate against the API service.
    
    Args:
        api_key (str): The API key to check
        
    Returns:
        bool: True if the key appears valid, False otherwise
    """
    if not api_key or not isinstance(api_key, str):
        return False
    
    # For Google API keys, they're typically ~40 characters
    if len(api_key) < 30:
        return False
    
    return True

# Conversation Management Functions
def save_conversation(messages, user_id=None):
    """
    Saves the current conversation to a file for later reference.
    
    Args:
        messages (list): List of message dictionaries
        user_id (str, optional): Unique identifier for the user
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs("conversation_history", exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        user_prefix = f"{user_id}_" if user_id else ""
        filename = f"conversation_history/{user_prefix}{timestamp}.json"
        
        # Save conversation to file
        with open(filename, "w") as f:
            json.dump(messages, f, indent=2)
        
        return True
    except Exception as e:
        print(f"Error saving conversation: {e}")
        return False

def load_conversation(filepath):
    """
    Loads a previously saved conversation.
    
    Args:
        filepath (str): Path to the conversation JSON file
        
    Returns:
        list: The conversation messages or empty list if not found
    """
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading conversation: {e}")
        return []

# Text Processing Functions
def extract_keywords(text, max_keywords=5):
    """
    Extracts key terms from the input text.
    This is a simplified version that splits by spaces and removes common words.
    
    Args:
        text (str): Input text
        max_keywords (int): Maximum number of keywords to extract
        
    Returns:
        list: Extracted keywords
    """
    # Simple list of common words to exclude
    common_words = set([
        "a", "an", "the", "and", "or", "but", "is", "are", "was", "were", 
        "in", "on", "at", "to", "for", "with", "by", "about", "like", 
        "through", "over", "before", "after", "under", "above", "between",
        "I", "you", "he", "she", "it", "we", "they", "this", "that", "these", "those",
        "my", "your", "his", "her", "its", "our", "their"
    ])
    
    # Tokenize and filter
    words = [word.lower() for word in text.split() if word.isalnum()]
    keywords = [word for word in words if word not in common_words]
    
    # Return up to max_keywords
    return keywords[:max_keywords]

# Performance Monitoring
def log_performance(function_name, start_time, end_time, status, details=None):
    """
    Logs the performance of a function for monitoring.
    
    Args:
        function_name (str): Name of the function being monitored
        start_time (float): Start time from time.time()
        end_time (float): End time from time.time()
        status (str): Status of the operation (success/failure)
        details (dict, optional): Additional details to log
    """
    try:
        duration = end_time - start_time
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "function": function_name,
            "duration_seconds": duration,
            "status": status
        }
        
        if details:
            log_entry.update(details)
        
        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        
        # Append to daily log file
        log_date = datetime.now().strftime("%Y-%m-%d")
        log_file = f"logs/performance_{log_date}.log"
        
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
    except Exception as e:
        print(f"Error logging performance: {e}") 