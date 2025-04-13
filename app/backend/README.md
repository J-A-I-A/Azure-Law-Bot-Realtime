# Backend Documentation

## Overview
The backend is a Python-based server that handles:
- Real-time chat processing
- Azure AI services integration
- Document processing and analysis
- WebSocket communication

## Directory Structure
```
backend/
├── app.py           # Main application entry point
├── ragtools.py      # RAG (Retrieval-Augmented Generation) tools
├── relevant_info.py # Information retrieval utilities
├── rtmt.py          # Real-time message processing
├── setup_intvect.py # Vector database setup
├── static/          # Static files directory
├── requirements.txt # Python dependencies
└── .env            # Environment variables
```

## Key Components

### app.py
- Main FastAPI application
- WebSocket endpoint for real-time communication
- REST API endpoints
- Error handling and logging

### ragtools.py
- Retrieval-Augmented Generation implementation
- Document processing and indexing
- Search functionality

### relevant_info.py
- Information extraction utilities
- Document analysis tools
- Context management

### rtmt.py
- Real-time message processing
- Chat history management
- Response generation

### setup_intvect.py
- Vector database initialization
- Document embedding setup
- Index management

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
   - Copy `.env.example` to `.env`
   - Fill in required API keys and configurations

## API Endpoints
- WebSocket: `/realtime` for real-time chat
- REST endpoints for document processing
- Health check endpoints

## Data Processing
- Document ingestion and processing
- Vector embeddings generation
- Context-aware response generation
- Real-time message handling

## Security
- Environment variable management
- API key protection
- Input validation
- Error handling

## Best Practices
- Follow Python coding standards (PEP 8)
- Implement proper error handling
- Use type hints
- Write comprehensive tests
- Document API endpoints
- Implement proper logging 