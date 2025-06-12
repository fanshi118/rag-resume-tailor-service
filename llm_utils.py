from langchain_community.chat_models import ChatOllama
from langchain.agents import load_tools, initialize_agent
from langchain.agents.agent_types import AgentType

def initialize_llm_and_agent():
    llm = ChatOllama(model="llama3.2")
    tools = load_tools(["requests_all"], llm=llm, allow_dangerous_tools=True)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return llm, agent
