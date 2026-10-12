from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-20b",
    temperature=0.1
)

# Prompt template
prompt = PromptTemplate(
    input_variables=[
        "problem_situation",
        "customer_name",
        "agent_name",
    ],
    template="""
You are a professional company customer-support representative.

Generate a professional and polite customer-support email.

Problem Situation:
{problem_situation}

Customer Name:
{customer_name}

Agent Name:
{agent_name}

Requirements:
- Use a professional and polite tone.
- Apologize to the customer for the inconvenience caused.
- Clearly acknowledge the customer's problem.
- Explain the solution or next steps.
- Keep the email under 5-6 sentences.
- End the email professionally.
"""
)

# User inputs
problem_situation = input("Enter the problem situation: ")
customer_name = input("Enter the customer name: ")
agent_name = input("Enter the agent name: ")

# Create final prompt
final_prompt = prompt.format(
    problem_situation=problem_situation,
    customer_name=customer_name,
    agent_name=agent_name
)

# Get response from LLM
response = llm.invoke(final_prompt)

print("\nAI Customer Support Email:\n")
print(response.content)