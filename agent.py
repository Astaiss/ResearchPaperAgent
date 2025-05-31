import os
import asyncio
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import openai
from google.adk.tools import FunctionTool
from .search import google_search_grounding as google_search


collect_from_google_search = LlmAgent(
    model="gemini-2.0-flash",
    name="GoogleSearchGrounding",
    description="An agent providing Google-search grounding capability",
    instruction="""
    You are a Reaseach Agent. You will be provided with a query and you will search the topic for research.
    """,
    tools=[google_search],
)

collect_papers_title_and_link = LlmAgent(
    model="gemini-2.0-flash",
    name="PapersTitleAndLinkAgent",
    description="An agent providing paper title and link collection capability",
    instruction="""
    You are a Reaseach Agent. You will be provided with a query and you will search for the answer using Google Search.
    From user query try to find the research papers and their titles and links. You should also provide resource references with links to the relevant research papers.
    """,
    tools=[google_search],
    
)


create_knowledge_graph = LlmAgent(
    model="gemini-2.0-flash",
    name="KnowledgeGraphAgent",
    description="An agent providing knowledge graph capability",
    instruction="""
    You are a Reaseach Agent. You will be provided with a query and you will search for the answer using Google Search.
    From user query try to construct a knowledge graph by finding the relationships between different entities. And provide the 
    user with a comprehensive knowledge graph that includes entities, relationships, and attributes with resource references.
    """,
    tools=[google_search],

    
)

find_research_gap = LlmAgent(
    model="gemini-2.0-flash",
    name="ResearchGapAgent",
    description="An agent providing research gap capability",
    instruction="""
    You are a Reaseach Agent. You will be provided with a query and you will search for the answer using Google Search.
    From user query try to identify the research gap in the existing literature and provide a comprehensive analysis of the research gap.
    You should also provide resource references with links to the relevant research papers.
    """,
    tools=[google_search],
    
)

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="ResearchAgent",
    description="An agent providing research capability",
    instruction="""
    You are the Root Agent. Your role is to understand the user's request and combine the rresults from various sub-agents to provide a comprehensive response.
    You will be provided with a query and you will search for the answer using Google Search.
    """,
    sub_agents=[
        collect_from_google_search,
        collect_papers_title_and_link,
        create_knowledge_graph,
        find_research_gap,
    ],
)