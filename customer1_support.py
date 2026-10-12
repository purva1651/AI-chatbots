import streamlit as st
import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()


# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")


# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="openai/gpt-oss-20b",
    temperature=0.1
)


# Page title
st.title("🏏 AI Customer Support ")

st.write(
    "Generate exciting, real-time customer support responses using AI."
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
st.subheader("Customer Support Details")


customer_name = st.text_input(
    "👤 Customer Name",
    placeholder="Enter customer name"
)


agent_name = st.text_input(
    "🤖 Agent Name",
    placeholder="Enter agent name"
)


problem_situation = st.text_area(
    "📋 Problem Situation",
    placeholder="Enter the problem situation...",
    height=150
)


# Generate button
if st.button("🎙️ Generate Commentary"):

    if not customer_name:
        st.warning("Please enter the customer name.")

    elif not agent_name:
        st.warning("Please enter the agent name.")

    elif not problem_situation:
        st.warning("Please enter the problem situation.")

    else:

        # Create final prompt
        final_prompt = prompt.format(
            problem_situation=problem_situation,
            customer_name=customer_name,
            agent_name=agent_name
        )

        # Generate response
        with st.spinner("Generating support email..."):

            try:
                response = llm.invoke(final_prompt)

                st.subheader("🎙️ AI Support Email")

                st.write(response.content)

            except Exception as e:

                st.error(f"Error: {e}")


