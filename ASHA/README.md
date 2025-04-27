# ASHA - AI Career Companion for Women

ASHA is an advanced AI career companion designed for the ASHA AI Hackathon 2025, specifically created to empower women in their professional journeys. ASHA acts as a personalized career mentor, providing tailored advice based on career stage, industry, and individual goals.

## Features

- **Career Stage Personalization**: Provides customized guidance for women who are:
  - Just starting their careers (Starters)
  - Returning after career breaks (Restarters)
  - Advancing in established careers (Risers)

- **Women-Focused Design**: Specifically built to address challenges faced by women in the workplace

- **Conversational Interface**: Natural, empathetic dialogue that mimics talking to a real mentor

- **Knowledge-Enhanced Responses**: Incorporates industry insights, career resources, and practical strategies

- **Private Sessions**: Maintains conversation history within the session only, respecting privacy

## Getting Started

### Prerequisites

- Python 3.8+
- Pip package manager

### Installation

1. Clone the repository (or download the source code)

2. Navigate to the project directory:
   ```bash
   cd ASHA
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. The application uses multiple API keys for Google Gemini model to optimize performance. These are included in the code.

### Running the Application

#### Easy Method (Windows)
Simply double-click the `run.bat` file in the ASHA directory.

#### Using the Launcher Script
```bash
python run.py
```

#### Manual Method
Start the Streamlit app directly:
```bash
streamlit run asha_chatbot.py
```

The application will open in your default web browser at `localhost:8501`

## Performance Optimizations

ASHA includes several optimizations to ensure smooth performance:

- **API Key Rotation**: Automatically rotates between multiple API keys to prevent rate limiting
- **Response Caching**: Caches common responses to reduce API calls
- **Failure Recovery**: Smart handling of API failures with automatic fallback
- **Cool-down Periods**: Implements cool-down for failed API keys to allow quota recovery

## Usage Examples

- **Career Planning**: "I'm looking to switch from marketing to product management. What skills should I develop?"

- **Resume Help**: "Can you help me highlight my achievements on my resume as I return to work after maternity leave?"

- **Work-Life Balance**: "How can I negotiate for flexible working arrangements while still advancing my career?"

- **Interview Preparation**: "What questions should I prepare for a senior management role in healthcare?"

- **Salary Negotiation**: "I'm not sure how to approach asking for a raise. Any tips?"

## Technology Stack

- **Frontend & Backend**: Streamlit
- **AI Model**: Google Gemini 1.5 Pro
- **Knowledge Base**: Custom-built career resources database
- **Context Management**: Session-based state management

## Project Structure

- `asha_chatbot.py`: Main application file with Streamlit interface
- `career_knowledge.py`: Knowledge base with career resources and industry insights
- `utils.py`: Utility functions for response enhancement and knowledge retrieval
- `requirements.txt`: Required Python dependencies
- `run.py`: Python launcher script with environment checks
- `run.bat`: Windows batch file for easy execution

## Ethical Considerations

- **Bias Mitigation**: Designed to avoid gender stereotypes and biases
- **Privacy-Focused**: No persistent storage of personal data
- **Career-Specific**: Redirects non-career conversations back to professional topics
- **Empowerment-Centered**: Focuses on building confidence and providing actionable advice

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the women who continue to break barriers in the workplace
- Created for the ASHA AI Hackathon 2025 