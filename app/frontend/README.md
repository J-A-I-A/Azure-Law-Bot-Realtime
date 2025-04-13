# Frontend Documentation

## Overview
The frontend is built using modern web technologies including:
- React 18 with TypeScript
- Vite as the build tool
- Tailwind CSS for styling
- Shadcn UI components (built on Radix UI)
- i18next for internationalization
- react-use-websocket for WebSocket communication

## Directory Structure
```
frontend/
├── src/            # Source code directory
├── public/         # Static assets
├── node_modules/   # Dependencies
├── package.json    # Project configuration and dependencies
├── tsconfig.json   # TypeScript configuration
├── vite.config.ts  # Vite configuration
├── tailwind.config.js  # Tailwind CSS configuration
├── postcss.config.js   # PostCSS configuration
├── components.json     # Shadcn UI configuration
└── .prettierrc        # Prettier configuration
```

## Key Features
- Real-time chat interface with WebSocket integration
- Modern, responsive design
- Type-safe development with TypeScript
- Component-based architecture
- Optimized build process with Vite
- Internationalization support
- Formatted code with Prettier

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

## Key Components
- Chat interface components
- Real-time message handling with WebSocket
- User input validation
- Error handling and loading states
- Internationalization components

## API Integration
The frontend communicates with the backend through:
- WebSocket connections for real-time updates (using react-use-websocket)
- REST API endpoints for data operations

## Styling
- Uses Tailwind CSS for utility-first styling
- Custom components built with Shadcn UI and Radix UI primitives
- Responsive design for all screen sizes
- Animation support with Framer Motion
- Dark/light mode support

## Best Practices
- Follow TypeScript best practices
- Use functional components with hooks
- Implement proper error boundaries
- Follow accessibility guidelines
- Write unit tests for components
- Use proper internationalization practices
- Follow consistent code formatting with Prettier 