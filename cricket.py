from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-20b",
    temperature=0.1
)

# Prompt template
prompt = PromptTemplate(
    input_variables=[
        "match_situation",
        "batsmen",
        "bowler",
    ],
    template="""
You are an energetic cricket commentator.

Generate exciting, dramatic and fast-paced cricket commentary.

Match Situation:
{match_situation}

Batsman Name:
{batsmen}

Bowler Name:
{bowler}

Requirements:
- The commentary should be in a friendly and exciting tone.
- keep the commentary under 350 words.
-Make it fell like the commentary is happening in real time.

"""
)

# User inputs
match_situation = input("Enter the match situation: ")
batsmen = input("Enter the batsman name: ")
bowler = input("Enter the bowler name: ")

# Create final prompt
final_prompt = prompt.format(
    match_situation=match_situation,
    batsmen=batsmen,
    bowler=bowler
)

# Get response from LLM
response = llm.invoke(final_prompt)

print("\nAI Commentary:\n")
print(response.content)