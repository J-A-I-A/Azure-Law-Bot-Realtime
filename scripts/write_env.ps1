# Define the .env file path
$envFilePath = "app\backend\.env"

# Clear the contents of the .env file
Set-Content -Path $envFilePath -Value ""

# Define the environment variables and their values
Add-Content -Path $envFilePath -Value "AZURE_OPENAI_ENDPOINT="
Add-Content -Path $envFilePath -Value "AZURE_OPENAI_REALTIME_DEPLOYMENT="
Add-Content -Path $envFilePath -Value "AZURE_OPENAI_REALTIME_VOICE_CHOICE="
Add-Content -Path $envFilePath -Value "PINECONE_API_KEY="
