"""
AI Engineer Portfolio - Main Application Entry Point

This file serves as the entry point for the AI Engineer Portfolio application.
It initializes the NiceGUI framework and starts the web server.
"""
import os
import sys
import codecs
from dotenv import load_dotenv
from nicegui import ui

# Force UTF-8 encoding for reliability
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Import the page definitions
import app.main  # noqa: F401

# Load environment variables from .env file (if present)
load_dotenv()

if __name__ in {"__main__", "__mp_main__"}:
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")

    ui.run(
        host=host,
        port=port,
        title="AI Engineer Portfolio",
        favicon="🤖",
        dark=True,
        uvicorn_logging_level='info',
        reload=False
    )