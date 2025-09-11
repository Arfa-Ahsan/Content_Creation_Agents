from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from posttrend.tools.search_tool import search_tool
import os
from dotenv import load_dotenv

@CrewBase
class Posttrend():
    """Posttrend crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Get API key from .env
        self.grok_llm = LLM(
        model="huggingface/meta-llama/Llama-3.3-70B-Instruct",   
        api_key=os.getenv("HF_TOKEN")
)
    @agent
    def media_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['media_analyst'],
            verbose=True,
            tools=[search_tool],
            llm=self.grok_llm,
           
        )
    
    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'],
            verbose=True,
            llm=self.grok_llm,
           
        )
    @agent
    def seo_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_optimizer'], 
            llm=self.grok_llm,
            verbose=True,
        )
    
    @task
    def analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyst_task'], 
            output_file='output/Finding_Trends.md',
            
        )
    
    @task
    def content_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_writer_task'],
            output_file='output/Content_Ideas.md',
            context=[self.analyst_task()],
        )
    
    @task
    def seo_optimizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_optimizer_task'],
            output_file='output/SEO_Optimized_Content.md',
            context=[self.content_writer_task()],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Posttrend crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
