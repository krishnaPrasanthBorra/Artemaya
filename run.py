import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if all required packages are installed"""
    try:
        import streamlit
        import google.generativeai
        import dotenv
        from PIL import Image
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        return False

def install_dependencies():
    """Install required packages"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Please run: pip install -r requirements.txt")
        return False

def start_app():
    """Start the Streamlit application"""
    print("Starting Artemaya application...")
    try:
        # Open browser automatically after a short delay
        url = "http://localhost:8501"
        webbrowser.open(url)
        
        # Start Streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
        return True
    except Exception as e:
        print(f"Error starting application: {e}")
        return False

if __name__ == "__main__":
    print("Artemaya - Initialization")
    print("-" * 40)
    
    # Check if dependencies are installed
    if not check_dependencies():
        print("Installing missing dependencies...")
        if not install_dependencies():
            sys.exit(1)
    
    # Start the application
    start_app() 