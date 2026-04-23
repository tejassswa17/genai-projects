from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompts.match_prompt import match_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

print("MATCH CHAIN FILE LOADED")  # debug

match_chain = match_prompt | llm