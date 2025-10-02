#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from posttrend.crew import Posttrend

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "top 5 agentic frameworks",
        "content_type":"Blog Post",   #["Blog Post", "LinkedIn Post", "Instagram Caption","Tiktok Caption","X Post"]
        'current_year': str(datetime.now().year)
    }
    
    try:
        Posttrend().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


