# Setting Up Artemaya

Follow these steps to set up and run the Artemaya AI assistant on your local machine.

## Prerequisites

- Python 3.8 or higher
- A Google Gemini API key

## Step 1: Get a Google Gemini API Key

1. Visit the [Google AI Studio](https://makersuite.google.com/)
2. Sign in with your Google account
3. Navigate to the API section
4. Create a new API key or use an existing one
5. Copy your API key for later use

## Step 2: Set Up Environment Variables

Create a `.env` file in the root directory of the project (same location as `app.py`) with the following content:

```
# Google Gemini API Keys
GOOGLE_API_KEY_1=your_api_key_here
```

Replace `your_api_key_here` with your actual Google Gemini API key.

Optional: For better performance and to avoid rate limits, you can add multiple API keys:

```
GOOGLE_API_KEY_1=your_first_api_key_here
GOOGLE_API_KEY_2=your_second_api_key_here
GOOGLE_API_KEY_3=your_third_api_key_here
```

## Step 3: Install Python Dependencies

1. Open a terminal or command prompt
2. Navigate to the project directory
3. Run: `pip install -r requirements.txt`

## Step 4: Run the Application

### On Windows:
Simply double-click the `run.bat` file in the project directory.

### Using Python:
Run the command: `python run.py`

The application will automatically open in your default web browser at `http://localhost:8501`.

## Troubleshooting

### API Key Issues
- If you see an error about API keys, make sure your `.env` file is correctly set up
- Ensure the API keys are valid and have not reached their quota limits

### Installation Problems
- If you encounter installation errors, try running: `pip install --upgrade pip` before installing requirements
- For Windows users, you might need to run the command prompt as Administrator

### Runtime Errors
- Check that all dependencies are installed correctly
- Ensure you're using a compatible Python version (3.8+)
- If you get a module not found error, try reinstalling the requirements 