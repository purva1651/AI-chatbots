import os
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from datetime import datetime

# Tool 1
@tool
def calculator(expression: str):
    """Useful for solving math problems."""
    return str(eval(expression))

@tool
def current_time(time:str):
    """useful for giving current date & time"""
    return datetime.now()

groq_api_key = os.getenv("GROQ_API_KEY")
# LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=groq_api_key
)

# Agent
agent = create_agent(
    model=llm,
    tools=[calculator, current_time],
    system_prompt="Use the current_time tool to answer date and time questions."
)

# Run
response = agent.invoke({
    "messages": [
        {"role": "user", "content": "who is the current time in Pacific?"},
    ]
})
print(response["messages"][-1].content)

