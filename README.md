# Azure Law Bot - Real-time

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
   - Obtain the `.env` file containing the necessary API keys
   - Place it in the `app/backend` directory

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

## Environment Variables Required
The `.env` file in the backend directory should contain:
- Azure credentials
- Other necessary API keys and configurations

## Troubleshooting
If you encounter any issues:
1. Ensure all dependencies are installed correctly
2. Verify the `.env` file is in the correct location
3. Check that the `static` directory exists in the backend folder
4. Make sure you're running the commands from the correct directory
5. For frontend issues:
   - Clear your npm cache: `npm cache clean --force`
   - Delete `node_modules` and run `npm install` again
   - Make sure you're using the correct Node.js version
