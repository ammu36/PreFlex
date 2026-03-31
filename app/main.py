from dotenv import load_dotenv
import logging
from fastapi import FastAPI, HTTPException

load_dotenv()

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Chatbot Preference & Context API",
    version="1.0",
    description="Plugin for personalized chatbot context generation using Gemini and FAISS."
)