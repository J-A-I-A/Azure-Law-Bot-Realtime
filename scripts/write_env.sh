#!/bin/bash

# Define the .env file path
ENV_FILE_PATH="app/backend/.env"

# Clear the contents of the .env file
> $ENV_FILE_PATH

# Append new values to the .env file
echo "AZURE_OPENAI_ENDPOINT=" >> $ENV_FILE_PATH
echo "AZURE_OPENAI_REALTIME_DEPLOYMENT=" >> $ENV_FILE_PATH
echo "AZURE_OPENAI_REALTIME_VOICE_CHOICE=" >> $ENV_FILE_PATH
echo "PINECONE_API_KEY=" >> $ENV_FILE_PATH
