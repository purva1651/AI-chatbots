import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=groq_api_key
)

def research_agent(topic):
    prompt = f"""
    you are a helpful research agent.summarize you research in less than 100 words 
    include real time examples

    Topic: {topic}
 """
    response = llm.invoke(prompt)
    return response.content

def review_agent(research):
    prompt = f"""
    you are a helpful review agent, look for mistakes and correct it,avoid unnecessary details and keep it concise, make sure to correct grammer, spelling, and punctuation errors. provide suggestions for improvement.
    include real time examples
    check for grammar, spelling, and punctuation errors. provide suggestions for improvement.

    Research: {research}

 """
    response = llm.invoke(prompt)
    return response.content

def multi_agent(topic):
    research = research_agent(topic)
    print("---Output from 1st Agent---")
    print(research)

    review = review_agent(research)
    print("---Output from 2nd Agent---")
    print(review)

multi_agent(input("Enter your topic here: "))