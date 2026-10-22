import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from multiagent import research_agent

from multiagent import research_agent

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=groq_api_key
)

def code_agent(task):
    prompt = f"""
    you are a helpful code agent. write a code in any language.
    Return ONLY the code.
    Do not explain how to do it.
    Do not include introductory sentences.
    Do not use Markdown code fences.
    Include comments only when necessary.
    Follow proper formatting and indentation.
    Use the most suitable programming language.  
    Task: {task}
 """
    response = llm.invoke(prompt)
    return response.content

def review_agent(code):
    prompt = f"""
    you are a helpful code review agent. 
    Return ONLY the complete corrected code.
    Do not explain your changes.
    Do not include introductory sentences.
    Do not use Markdown code fences.
    Follow proper formatting and indentation.
    Preserve the original programming language.
    If the code is already correct, return it unchanged
    Code: {code}

 """
    response = llm.invoke(prompt)
    return response.content

def multi_agent(task):
    code = code_agent(task)
    print("---Output from 1st Agent---")
    print(code)

    review = review_agent(code)
    print("---Output from 2nd Agent---")
    print(review)

multi_agent(input("Enter your task here: "))