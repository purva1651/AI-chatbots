#travel iternary-AI Travel expense
#destination,no of person,no of days,travel type,,budget,accommodation type 
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
    temperature=0.1
)


# Page title
st.title("AI Travel Planner")

st.write(
    "Plan your perfect trip with the help of AI."
)


# Prompt template
prompt = PromptTemplate(
    input_variables=[
        "destination",
        "no_of_persons",
        "no_of_days",
        "travel_type",
        "budget",
        "accommodation_type"
    ],

    template="""
Create personalized day-wise travel itineraries.

Estimate trip expenses, and plan your journey within budget.

destination:
{destination}

no_of_persons:
{no_of_persons}

no_of_days:
{no_of_days}

travel_type:
{travel_type}

budget:
{budget}

accommodation_type:
{accommodation_type}

Requirements:
Requirements:

- Create a personalized travel itinerary.
- Include a day-wise travel  plan in tabular format.
- Make this plan according to one person in budget and accommodation type.
- Suggest places to visit and activities.
- Recommend famous local food and transport.
-Also recommend the viral food of that place.
- Estimate accommodation, food, and travel costs.
- Calculate the total trip expense.
- when you say about the budget say in that country currency and also mention the currency name.
- Consider the number of travelers and trip duration.
- Keep the response under 350 words.
- Use simple language and clear headings and friendly tone.
"""
)


# User inputs
st.subheader("Travel Details")


destination = st.text_input(
    "Destination place",
    placeholder="Enter destination plan"
)


no_of_persons = st.text_input(
    "Total Number of persons",
    placeholder="Enter Number of persons"
),

no_of_days = st.text_input(
    "Number of Days",
    placeholder="Enter Number of Days"
)

travel_type = st.text_input(
    "Travel type",
    placeholder="Type of Travel"
)

budget = st.text_input(
    "Budget",
    placeholder="Enter budget"
)

accommodation_type = st.text_input(
    "Accomodation Type",
    placeholder="Accommodation Type"
)

# Generate button
if st.button("Generate Iternary Plan"):

    if not destination:
        st.warning("Please enter the destination.")

    elif not no_of_persons:
        st.warning("Please enter the number of persons.")

    elif not no_of_days:
        st.warning("Please enter the number of days.")

    elif not travel_type:
        st.warning("Please enter the travel type.")

    elif not budget:
        st.warning("Please enter the budget.")

    elif not accommodation_type:
        st.warning("Please enter the accommodation type.")


    else:

        # Create final prompt
        final_prompt = prompt.format(
            destination=destination,
            no_of_persons=no_of_persons,
            no_of_days=no_of_days,
            travel_type=travel_type,
            budget=budget,
            accommodation_type=accommodation_type
        )

        # Generate response
        with st.spinner("Generating iternary plan for the trip..."):

            try:
                response = llm.invoke(final_prompt)

                st.subheader("AI Iternary Plan")

                answer = (response.content)

                typing_placeholder = st.empty()

                displayed_text = ""

                for char in answer:
                    displayed_text += char
                    typing_placeholder.markdown(displayed_text + "▌")
                    time.sleep(0.01)


            except Exception as e:

                st.error(f"Error: {e}")
