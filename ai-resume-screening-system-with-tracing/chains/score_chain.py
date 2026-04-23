from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompts.score_prompt import score_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

score_chain = score_prompt | llm