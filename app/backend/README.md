# Backend Documentation

## Overview
The backend is a Python-based server that handles:
- Voice-enabled real-time chat processing with WebSocket
- Azure OpenAI services integration for:
  - Real-time audio transcription
  - Text-to-speech synthesis
  - LLM inference with tool capabilities
- Retrieval-Augmented Generation (RAG) with legal document search
- Pinecone vector database integration for document retrieval

## Directory Structure
```
backend/
├── app.py           # Main FastAPI application with WebSocket endpoint
├── ragtools.py      # RAG tools implementation for document search
├── relevant_info.py # Pinecone vector database search implementation
├── rtmt.py          # Real-time message processing (middle-tier between client and Azure)
├── setup_intvect.py # Vector database setup and document indexing
├── static/          # Static files directory for serving frontend
├── requirements.txt # Python dependencies
└── .env            # Environment variables
```

## Key Components

### app.py
- Main application entry point using aiohttp
- WebSocket endpoint (`/realtime`) for real-time communication
- Static file serving for frontend
- Azure OpenAI integration with credentials management
- Error handling and logging

### ragtools.py
- Implements tools for the LLM to use during conversations
- Search tool for retrieving relevant legal information
- Integration with the `relevant_info.py` module for document search
- Format conversion between Azure OpenAI and client

### relevant_info.py
- Connects to Pinecone vector database
- Retrieves relevant documents using embedding-based search
- Reranks search results using LLM
- Returns formatted JSON with document chunks and metadata

### rtmt.py (Real-Time Middle Tier)
- Manages WebSocket communication between client and Azure OpenAI
- Handles tool calling functionality
- Processes speech-to-text and text-to-speech
- Manages session state and configuration
- Routes messages between client and Azure OpenAI

### setup_intvect.py
- Sets up Azure Cognitive Search index
- Configures embedding pipeline for documents
- Uploads documents to Azure Blob Storage
- Creates indexers and skillsets for document processing

## Environment Setup
1. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file with the following variables:
     ```
     AZURE_OPENAI_API_KEY=your_api_key
     AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com
     AZURE_OPENAI_REALTIME_DEPLOYMENT=your_deployment_name
     AZURE_OPENAI_REALTIME_VOICE_CHOICE=alloy  # Optional, defaults to alloy
     PINECONE_API_KEY=your_pinecone_api_key
     ```

## WebSocket Communication
The backend implements a bidirectional WebSocket connection at the `/realtime` endpoint that:
1. Receives audio data from the client
2. Forwards it to Azure OpenAI's real-time API
3. Processes responses and tool calls
4. Returns both text responses and audio synthesis to the client

## Document Processing
- Documents are stored in Pinecone vector database
- Each search query is converted to embeddings
- Relevant documents are retrieved and reranked
- Results are returned to the LLM for context-aware responses

## Starting the Server
Run the server with:
```bash
python app.py
```
The server will start on http://localhost:8765

## Security Considerations
- Environment variable management for API keys
- Azure authentication using AzureKeyCredential or DefaultAzureCredential
- Input validation for WebSocket messages
- Error handling and logging

## Best Practices
- Follow Python coding standards (PEP 8)
- Use of type hints throughout the codebase
- Asynchronous programming with asyncio and aiohttp
- Structured error handling
- Comprehensive logging 