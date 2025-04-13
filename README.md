# Azure Law Bot - Real-time

## Overview
This application is a voice-enabled legal assistant that provides real-time responses using Azure AI services. It features:
- Real-time voice-to-text and text-to-voice communication
- Legal document searching and grounding responses in source documents
- WebSocket-based communication for real-time interactions

## Prerequisites

Ensure you have the required software installed:

- Node.js (version 23.x or higher) for the front end
- Python (version 3.11 or higher) for the back end

## Backend Setup

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd Azure-Law-Bot-Realtime
   ```

2. Set up Python environment:
   ```bash
   # Make the setup script executable
   chmod +x scripts/load_python_env.sh
   
   # Run the setup script to create virtual environment
   ./scripts/load_python_env.sh
   ```

3. Environment Variables:
   - Obtain the `.env` file containing the necessary API keys (Azure OpenAI API keys and endpoint URLs)
   - Place it in the `app/backend` directory
   - Required environment variables include:
     - AZURE_OPENAI_API_KEY
     - AZURE_OPENAI_ENDPOINT
     - AZURE_OPENAI_REALTIME_DEPLOYMENT
     - AZURE_OPENAI_REALTIME_VOICE_CHOICE (optional, defaults to "alloy")

4. Install Dependencies:
   ```bash
   cd app/backend
   pip install -r requirements.txt
   ```

5. Create Static Directory:
   ```bash
   mkdir -p static
   ```

6. Run the Backend Server:
   ```bash
   python app.py
   ```
   The server will start at http://localhost:8765

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd app/frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will start at http://127.0.0.1:5173

4. For production build:
   ```bash
   npm run build
   ```

## API Endpoints

- WebSocket: `/realtime` - Handles real-time audio communication and chat functionality
- Static Files: `/` - Serves the frontend application

## Docker Development Setup

As an alternative to the manual setup above, you can use Docker for development:

1. Build the Docker image:
   ```bash
   docker build -t azure-law-bot -f app/Dockerfile .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 --env-file app/backend/.env azure-law-bot
   ```
   The application will be available at http://localhost:8000

Note: When using Docker, make sure your `.env` file is properly configured in the `app/backend` directory before building the image.

## Key Features
- Voice-based interaction with AI assistant
- Real-time transcription of voice input
- Audio playback of AI responses
- Document grounding with source attribution
- Interactive UI for viewing referenced documents

## Troubleshooting
If you encounter any issues:
1. Ensure all dependencies are installed correctly
2. Verify the `.env` file is in the correct location and contains all required keys
3. Check that the `static` directory exists in the backend folder
4. Make sure you're running the commands from the correct directory
5. For frontend issues:
   - Clear your npm cache: `npm cache clean --force`
   - Delete `node_modules` and run `npm install` again
   - Make sure you're using the correct Node.js version
6. For WebSocket connection issues:
   - Check that the backend is running on port 8765
   - Verify network connectivity between frontend and backend
