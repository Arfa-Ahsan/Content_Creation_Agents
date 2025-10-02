from crewai_tools import SerperDevTool,TavilySearchTool
from dotenv import load_dotenv
import os
from tavily import TavilyClient

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("SERPER_API_KEY")
tavily_api_key = os.getenv("TAVILY_SEARCH_API_KEY")

# Create tools
search_tool = SerperDevTool(api_key=api_key)
tavily_search_tool= TavilySearchTool(api_key=tavily_api_key)


