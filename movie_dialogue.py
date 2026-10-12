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
        "movie",
        "actor",
    ],
    template="""
You are an Script Writer.

Generate an original movie dialogue.

Movie Name:
{movie}

Actor Name:
{actor}

Requirements:

- Review the movie in a friendly and exciting tone.
- Keep the review under 250 words.
- Give the top 5 memorable dialogue moments from the movie.
- Summarize the dialogue moments instead of reproducing the exact movie dialogue.
- Explain briefly why each dialogue moment is memorable.
- Give the output in bullet-point format.
-Mix of hindi and english language in the output.
"""
)

# User inputs
movie = input("Enter the movie name: ")
actor = input("Enter the actor name: ")

# Create final prompt
final_prompt = prompt.format(
    movie=movie,
    actor=actor
)

# Get response from LLM
response = llm.invoke(final_prompt)

print("\nAI Movie Review:\n")
print(response.content)