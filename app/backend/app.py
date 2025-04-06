import logging
import os
from pathlib import Path

from aiohttp import web
from dotenv import load_dotenv

from ragtools import attach_rag_tools
from rtmt import RTMiddleTier
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("voicerag")

async def create_app():
    if not os.environ.get("RUNNING_IN_PRODUCTION"):
        logger.info("Running in development mode, loading from .env file")
        load_dotenv()

    llm_key = os.environ.get("AZURE_OPENAI_API_KEY")
    if not llm_key:
        logger.error("AZURE_OPENAI_API_KEY is not set")
        raise ValueError("AZURE_OPENAI_API_KEY is not set")
    
    credential = DefaultAzureCredential()
    llm_credential = AzureKeyCredential(llm_key) if llm_key else credential     
    app = web.Application()

    rtmt = RTMiddleTier(
        credentials=llm_credential,
        endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        deployment=os.environ["AZURE_OPENAI_REALTIME_DEPLOYMENT"],
        voice_choice=os.environ.get("AZURE_OPENAI_REALTIME_VOICE_CHOICE") or "alloy"
        )
    rtmt.system_message = """
        You are a helpful assistant.Only Speak and answer questions based on information you searched in the knowledge base in ENGLISH, accessible with the 'search' tool.
        When using the 'search tool' use a detailed sentence of the information you want to find.
        The user is listening to answers with audio, so it's *super* important that answers are as DETAILED as possible, never say just a single sentence if at all possible. 
        Never read file names or source names or keys out loud. 
        Always use the following step-by-step instructions to respond: 
        1. Always use the 'search' tool to check the knowledge base before answering a question. 
        2 Produce an answer that's as detailed as possible. If the answer isn't in the knowledge base, say you don't know. 
    """.strip()

    attach_rag_tools(rtmt)

    rtmt.attach_to_app(app, "/realtime")

    current_directory = Path(__file__).parent
    app.add_routes([web.get('/', lambda _: web.FileResponse(current_directory / 'static/index.html'))])
    app.router.add_static('/', path=current_directory / 'static', name='static')
    
    return app

if __name__ == "__main__":
    host = "localhost"
    port = 8765
    web.run_app(create_app(), host=host, port=port)
