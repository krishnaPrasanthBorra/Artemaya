# Artemaya

An AI-powered virtual assistant by Krishna Prasanth Borra.

## Description
Artemaya is an intelligent virtual assistant built using Google's Gemini AI model. It provides conversational assistance and can be personalized for various use cases.

## Features
- **Intelligent Conversations**: Engage in natural, flowing conversations with the AI assistant.
- **Context Awareness**: The assistant remembers the conversation history for more coherent interactions.
- **Modern UI**: Clean, responsive interface that works on both desktop and mobile devices.
- **API Key Rotation**: Built-in support for multiple API keys to prevent rate limiting.
- **Error Handling**: Graceful error handling and fallback mechanisms for a smooth user experience.
- **Conversation Management**: Save conversations for later reference.
- **Performance Logging**: Built-in performance monitoring.

## Technologies Used
- **Frontend**: Streamlit
- **AI Model**: Google Gemini 1.5 Pro
- **Language**: Python
- **Styling**: Custom CSS

## Getting Started
See [SETUP.md](SETUP.md) for detailed instructions on setting up and running the project.

### Quick Start
1. Clone this repository
2. Create a `.env` file with your Google Gemini API key(s)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python run.py` or use the `run.bat` file on Windows

## Project Structure
- `app.py`: Main application file containing the Streamlit interface and AI logic
- `utilities.py`: Helper functions for API key management, conversation saving, and performance logging
- `run.py`: Launcher script with dependency checking and browser automation
- `run.bat`: Windows batch file for easy execution
- `style.css`: Custom styling for the Streamlit application
- `requirements.txt`: Python dependencies
- `SETUP.md`: Detailed setup instructions
- `.env`: Environment variables (not included in repository)

## Future Enhancements
- Support for file uploads and analysis
- Voice input and output capabilities
- Integration with external knowledge bases
- Customizable themes and appearance settings
- User authentication and personalized experiences

## License
This project is open source and available under the MIT License.

## Acknowledgments
- Google Gemini for providing the AI model
- Streamlit for the web application framework 