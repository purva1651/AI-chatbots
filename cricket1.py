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
st.title("🏏 AI Cricket Commentator")

st.write(
    "Generate exciting, real-time cricket commentary using AI."
)


# Prompt template
prompt = PromptTemplate(
    input_variables=[
        "match_situation",
        "batsman",
        "bowler"
    ],

    template="""
You are an energetic cricket commentator.

Generate exciting, dramatic and fast-paced cricket commentary.

Match Situation:
{match_situation}

Batsman Name:
{batsman}

Bowler Name:
{bowler}

Requirements:

- The commentary should be in a friendly and exciting tone.
- Keep the commentary under 350 words.
- Make it feel like the commentary is happening in real time.
- Use cricket terminology naturally.
"""
)


# User inputs
st.subheader("Match Details")


batsman = st.text_input(
    "🏏 Batsman Name",
    placeholder="Enter batsman name"
)


bowler = st.text_input(
    "⚡ Bowler Name",
    placeholder="Enter bowler name"
)


match_situation = st.text_area(
    "📋 Match Situation",
    placeholder="Enter the current match situation...",
    height=150
)


# Generate button
if st.button("🎙️ Generate Commentary"):

    if not batsman:
        st.warning("Please enter the batsman name.")

    elif not bowler:
        st.warning("Please enter the bowler name.")

    elif not match_situation:
        st.warning("Please enter the match situation.")

    else:

        # Create final prompt
        final_prompt = prompt.format(
            match_situation=match_situation,
            batsman=batsman,
            bowler=bowler
        )

        # Generate response
        with st.spinner("Generating commentary..."):

            try:
                response = llm.invoke(final_prompt)

                st.subheader("🎙️ AI Dialogue")

                st.write(response.content)

            except Exception as e:

                st.error(f"Error: {e}")


