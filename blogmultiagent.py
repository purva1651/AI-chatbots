import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=groq_api_key
)

def writer(topic):
    prompt = f"""
    - Start with a clear, attractive title.
    - Write an engaging introduction.
    - Explain the topic in simple, understandable language.
    - Organize the content using meaningful headings.
    - Include practical examples and real-world applications.
    - Explain benefits, limitations, and challenges.
    - End with a strong conclusion.
    - Avoid repetition, vague claims, and unnecessary filler.
    - Use correct grammar, spelling, and punctuation.
    - Separate paragraphs and sentences with proper spacing.
    - Aim for approximately 150 words.
    Return only the blog post.
    Topic : {topic}
 """
    response = llm.invoke(prompt)
    return response.content

def editor(blog):
    prompt = f"""
    - Improve the structure and flow of ideas.
    - Remove repetitive or irrelevant sentences.
    - Replace vague wording with specific explanations.
    - Improve readability and engagement.
    - Check the title, headings, and paragraph structure.
    - Correct grammar, spelling, punctuation, and spacing.
    - Preserve useful examples and the author's intended meaning.
    - Do not invent statistics, facts, or sources.
    - Do not rewrite sentences that are already effective.

    Return only the complete edited blog post.
    Blog : {blog}

 """
    response = llm.invoke(prompt)
    return response.content

def reviewer(editorview):
    prompt = f"""
    You are a critical content reviewer.

    Review the edited blog below before publication.

    Check for:
    - Claims that may be inaccurate or misleading.
    - Unsupported statistics or statements.
    - Missing context or important limitations.
    - Contradictions and logical inconsistencies.
    - Repetition, unclear explanations, and formatting issues.
    - Whether the article actually answers the topic.

    Make corrections only when necessary.
    Never invent evidence or claim that you verified facts
    using external sources when you did not.
    Preserve accurate and well-written content.

    Return only the final, publication-ready blog post.
    Do not include your review notes.

    Blog : {editorview}

 """
    response = llm.invoke(prompt)
    return response.content


def multi_agent(topic):
    blog = writer(topic)
    print("---Output from 1st Agent---")
    print(blog)

    editorview = editor(blog)
    print("---Output from 2nd Agent---")
    print(editorview)

    Final_Output = reviewer(editorview)
    print("----output from 3rd agent---")
    print(Final_Output)


multi_agent(input("Enter your Topic  here: "))