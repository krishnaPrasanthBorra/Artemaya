#!/usr/bin/env python
"""
ASHA Launcher Script
This script provides an easy way to start the ASHA chatbot application.
"""

import os
import subprocess
import sys

def main():
    """Launch the ASHA chatbot application"""
    print("Starting ASHA - AI Career Companion...")
    
    # Check if Streamlit is installed
    try:
        import streamlit
        print("Streamlit detected. ✓")
    except ImportError:
        print("Error: Streamlit not installed.")
        print("Please install the requirements first using:")
        print("pip install -r requirements.txt")
        return
    
    # Check if required packages are installed
    try:
        import google.generativeai
        import dotenv
        import PIL
        print("All required packages detected. ✓")
    except ImportError as e:
        print(f"Error: Missing required package - {str(e)}")
        print("Please install the requirements first using:")
        print("pip install -r requirements.txt")
        return
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Launch Streamlit app
    try:
        print("\nLaunching ASHA application...")
        print("Once loaded, ASHA will be available in your browser.")
        print("Use Ctrl+C to stop the application.")
        print("\n" + "="*50)
        
        streamlit_cmd = [sys.executable, "-m", "streamlit", "run", 
                         os.path.join(current_dir, "asha_chatbot.py"),
                         "--server.headless", "false"]
        
        subprocess.run(streamlit_cmd)
    except KeyboardInterrupt:
        print("\nASHA application stopped.")
    except Exception as e:
        print(f"\nError launching ASHA: {str(e)}")
        return

if __name__ == "__main__":
    main() 