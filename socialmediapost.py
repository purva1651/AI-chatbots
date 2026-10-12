#topic,which platform,post length,target_audience,post tone,post format
#relevant hashtags
import streamlit as st
import os
from datetime import datetime
import time

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
    temperature=0.5
)


# Page title
st.title("AI Social Media Post Generator")

st.write(
    "Create engaging social media posts with the help of AI."
)


# Prompt template
prompt = PromptTemplate(
    input_variables=[
        "Topic",
        "platform",
        "post_length",
        "target_audience",
        "post_tone",
        "post_format"
    ],

    template="""
Create professional social media posts


Topic:
{Topic}

platform:
{platform}

post_length:{post_length}
-make the post into the desired length.

target_audience:
{target_audience}

post_tone:
{post_tone}

post_format:
{post_format}

Requirements:

- Create a personalized social media post.
- Use simple language and clear headings and friendly tone.
- make sure to include relevant hashtags and emojis which is appropriate for the platform.
- make to use validate information and provide accurate details for the topics.
-check proper grammar and spelling.
"""
)


# User inputs
st.subheader("Travel Details")


Topic = st.text_input(
    "Topic",
    placeholder="Enter topic"
)

platform = st.text_input(
    "Platform",
    placeholder="Enter platform"
)

post_length = st.text_input(
    "Post Length",
    placeholder="Enter post length"
)

target_audience = st.text_input(
    "Target Audience",
    placeholder="Enter target audience"
)

post_tone = st.text_input(
    "Post Tone",
    placeholder="Enter post tone"
)

post_format = st.text_input(
    "Post Format",
    placeholder="Enter post format"
)


# Generate button
if st.button("Generate Social Media Post"):

    if not Topic:
        st.warning("Please enter the topic.")

    elif not platform:
        st.warning("Please enter the platform.")

    elif not post_length:
        st.warning("Please enter the post length.")

    elif not target_audience:
        st.warning("Please enter the target audience.")

    elif not post_tone:
        st.warning("Please enter the post tone.")

    elif not post_format:
        st.warning("Please enter the post format.")

    else:

        # Create final prompt
        final_prompt = prompt.format(
            Topic=Topic,
            platform=platform,
            post_length=post_length,
            target_audience=target_audience,
            post_tone=post_tone,
            post_format=post_format
        )

        # Generate response
        with st.spinner("Generating social media post..."):

            try:
                response = llm.invoke(final_prompt)

                st.subheader("AI Social Media Post")

                answer = (response.content)

                typing_placeholder = st.empty()

                displayed_text = ""

                for char in answer:
                    displayed_text += char
                    typing_placeholder.markdown(displayed_text + "▌")
                    time.sleep(0.01)


            except Exception as e:

                st.error(f"Error: {e}")
