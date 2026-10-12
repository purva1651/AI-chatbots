import streamlit as st
import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()


# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")


# Check API key
if not groq_api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()


# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="openai/gpt-oss-20b",
    temperature=0.1
)


# Page title
st.title(" AI Movie Dialogue Generator")

st.write(
    "Generate exciting, real-time movie dialogue using AI."
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
- Mix of hindi and english language in the output.
"""
)


# User inputs
st.subheader("Movie Info")


movie = st.text_input(
    "� Movie Name",
    placeholder="Enter movie name"
)


actor = st.text_input(
    "🌟 Actor Name",
    placeholder="Enter actor name"
)

# Generate button
if st.button("🎙️ Generate Dialogue"):

    if not movie:
        st.warning("Please enter the movie name.")

    elif not actor:
        st.warning("Please enter the actor name.")


    else:

        # Create final prompt
        final_prompt = prompt.format(
            movie=movie,
            actor=actor
        )

        # Generate response
        with st.spinner("Generating dialogue..."):

            try:
                response = llm.invoke(final_prompt)

                st.subheader("🎙️ AI Dialogue")

                st.write(response.content)

            except Exception as e:

                st.error(f"Error: {e}")