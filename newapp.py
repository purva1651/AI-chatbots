import streamlit as st
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pypdf  import PdfReader
load_dotenv()

st.title("My LLM Chatbot")

file = st.file_uploader("Upload a file", type=["pdf"])
if file:
   text="".join([page.extract_text() for page in PdfReader(file).pages])

   question = st.text_input("Ask a question")

   if question:
     llm = ChatGroq(
       model="openai/gpt-oss-20b",
       api_key=os.getenv("GROQ_API_KEY"),
     )
       
     prompt= f"""
       You are a friendly RAG AI assistant.whenever user ask a question,you should answer in polite and friendly manner.
       Always give output in bullet points.
       Your Document:
       {text}

       Question: 
       {question}
       """
     st.write(llm.invoke(prompt).content)