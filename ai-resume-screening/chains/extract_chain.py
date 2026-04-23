from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompts.extract_prompt import extract_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# 👇 THIS LINE IS IMPORTANT
extract_chain = extract_prompt | llm