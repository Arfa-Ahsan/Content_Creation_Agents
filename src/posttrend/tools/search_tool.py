from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("SERPER_API_KEY")

# Create tools
search_tool = SerperDevTool(api_key=api_key)


