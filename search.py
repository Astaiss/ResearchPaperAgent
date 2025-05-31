from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from google.adk.tools import google_search

_search_agent = Agent(
    model="gemini-2.0-flash",
    name="GoogleSearchGrounding",
    description="An agent providing Google-search grounding capability",
    instruction=""",
    You are a Reaseach Agent. You will be provided with a query and you will search for the answer using Google Search.
    You may need to use google scholars to find the most relevant research papers and give the link of the website where you found.
    You will be provided with a query and you will search for the answer using Google Search.
    """,
    tools=[google_search],
)

google_search_grounding = AgentTool(agent=_search_agent)