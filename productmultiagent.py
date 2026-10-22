#1.Product search,price analyst,review analyst and recommendations
import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=groq_api_key
)

def product_search(requirements):
    prompt = f"""
    you are product search analyst 

    Find suitable products based on the user's requirements.

    Identify relevant product categories.
    Include brand and model names when known.
    Explain the key features of each product.
    Consider the user's budget and intended use.
    Include official product or retailer links only when known.
    Do not invent products, prices, or URLs.
    If live search data is unavailable, clearly say so.
    Separate verified information from general suggestions.
    Requirements : {requirements}
  """
    response = llm.invoke(prompt)
    return response.content

def price_analyst(products):
    prompt = f"""
    You are a Product Price Analyst.

    Analyze the products found by the search agent.

    - Compare prices when reliable prices are provided.
    - Consider features, specifications, and build quality.
    - Identify budget, mid-range, and premium options
      when the available data supports those categories.
    - Explain which product offers the best value for money.
    - Consider warranty, maintenance, and running costs
      when relevant and supported by available information.
    - Never invent current prices or discounts.
    - Do not assume that the cheapest product is the best.
    - State clearly when prices are estimates or unavailable.

    Products:
    {products}

    Return a structured price comparison and analysis.
  """
    response = llm.invoke(prompt)
    return response.content


# AGENT 3: PRODUCT REVIEWER
def review_product(price_analysis):
    prompt = f"""
    You are a Critical Product Review Agent.

    Evaluate the shortlisted products objectively.

    - Explain the major advantages of each product.
    - Identify limitations and possible disadvantages.
    - Assess usability, durability, and performance
      only where sufficient information is available.
    - Compare product specifications when provided.
    - Identify missing information that could affect a purchase.
    - Do not invent customer reviews or ratings.
    - Do not claim to have tested products personally.
    - Distinguish known facts from reasonable assessments.
    - Consider the user's needs and budget.

    Price Analysis:
    {price_analysis}

    Return a balanced review with pros, cons,
    and important purchasing considerations.
  """
    response = llm.invoke(prompt)
    return response.content


# AGENT 4: PRODUCT RECOMMENDATION
def recommendations(reviews):
    prompt = f"""
    You are a Product Recommendation Agent.

    Use the findings from the previous agents to make
    a personalized final recommendation.

    - Recommend the best overall product for the user.
    - Give a clear explanation for the recommendation.
    - Suggest a budget alternative if appropriate.
    - Suggest a premium alternative if it offers meaningful
      additional benefits.
    - Explain the main trade-offs between the options.
    - Respect the user's budget and intended use.
    - Do not invent specifications, prices, or reviews.
    - If the evidence is insufficient, say so.
    - Do not automatically select the most expensive product.

    Product Reviews:
    {reviews}

    Return the final recommendation using these headings:
    1. Best Overall Product
    2. Why It Is Recommended
    3. Pros and Cons
    4. Best Budget Alternative
    5. Best Premium Alternative
    6. Final Buying Advice

    Return only the final recommendation.
  """
    response = llm.invoke(prompt)
    return response.content


# MAIN MULTI-AGENT WORKFLOW
def multi_agent(requirements):

    # First Agent
    products = product_search(requirements)
    print("\n--- OUTPUT FROM AGENT 1: PRODUCT SEARCH ---")
    print(products)

    # Second Agent
    price_analysis = price_analyst(products)
    print("\n--- OUTPUT FROM AGENT 2: PRICE ANALYST ---")
    print(price_analysis)

    # Third Agent
    reviews = review_product(price_analysis)
    print("\n--- OUTPUT FROM AGENT 3: PRODUCT REVIEWER ---")
    print(reviews)

    # Fourth Agent
    final_output = recommendations(reviews)

    print("\n--- OUTPUT FROM AGENT 4: RECOMMENDATIONS ---")
    print(final_output)

    return final_output


multi_agent(input("enter your requirements"))
