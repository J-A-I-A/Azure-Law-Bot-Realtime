# Frontend Documentation

## Overview
The frontend is a voice-enabled legal assistant interface built with modern web technologies including:
- React 18 with TypeScript
- Vite as the build tool
- Tailwind CSS for styling
- Shadcn UI components (built on Radix UI)
- i18next for internationalization
- react-use-websocket for real-time communication

## Directory Structure
```
frontend/
├── src/
│   ├── components/     # UI and audio components
│   │   ├── audio/      # Audio recording and playback
│   │   └── ui/         # UI components using Shadcn/Radix
│   ├── hooks/          # Custom React hooks
│   │   ├── useRealtime.tsx     # WebSocket communication
│   │   ├── useAudioPlayer.tsx  # Audio playback
│   │   └── useAudioRecorder.tsx # Audio recording
│   ├── locales/        # i18n translation files
│   ├── i18n/           # i18n configuration
│   ├── assets/         # Static assets
│   ├── lib/            # Utility functions
│   ├── types.ts        # TypeScript type definitions
│   ├── App.tsx         # Main application component
│   └── index.tsx       # Application entry point
├── public/             # Static assets
├── node_modules/       # Dependencies
├── package.json        # Project configuration and dependencies
├── tsconfig.json       # TypeScript configuration
├── vite.config.ts      # Vite configuration
├── tailwind.config.js  # Tailwind CSS configuration
├── postcss.config.js   # PostCSS configuration
├── components.json     # Shadcn UI configuration
└── .prettierrc        # Prettier configuration
```

## Key Features
- Voice-to-text recording with real-time WebSocket streaming
- Text-to-speech playback of AI responses
- Internationalization support with multiple languages (English, Spanish, French, Japanese)
- Document grounding with source attribution
- Responsive design that works on all devices
- Interactive UI for viewing referenced legal documents

## WebSocket Communication
The application uses a WebSocket connection to the backend server for real-time communication:
- Audio data is collected, converted to base64, and sent to the backend
- The backend processes the audio and returns both text and audio responses
- Document references are displayed in the UI when returned from search results

## Development Setup
1. Install dependencies:
   ```bash
   npm install
   ```

2. Start development server:
   ```bash
   npm run dev
   ```
   The server will start at http://127.0.0.1:5173

3. Build for production:
   ```bash
   npm run build
   ```

4. Preview production build:
   ```bash
   npm run preview
   ```

5. Format code:
   ```bash
   npm run format
   ```

## Audio Processing
The frontend implements two main audio-related components:
- Audio recording: Captures microphone input, buffers it, and streams to the backend
- Audio playback: Processes returned audio data for real-time playback

## UI Components
The main UI components include:
- Microphone toggle for starting/stopping conversation
- Status indicator for recording state
- Document viewer for displaying search results
- File selection interface for viewing document content

## Internationalization
The application supports multiple languages using i18next:
- English (en)
- Spanish (es)
- French (fr)
- Japanese (ja)

Language files are stored in the `src/locales` directory.

## Best Practices
- Follow TypeScript best practices with proper type definitions
- Use functional components with React hooks
- Implement responsive design with Tailwind CSS
- Follow accessibility guidelines with Radix UI primitives
- Maintain clean code formatting with Prettier 