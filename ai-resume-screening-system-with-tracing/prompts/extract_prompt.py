from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate.from_template("""
You are an AI resume parser.

Extract:
1. Skills
2. Tools
3. Experience

Rules:
- Do NOT assume anything
- Only extract from text
- If missing → "Not mentioned"

Return ONLY JSON:

{{
  "skills": [],
  "tools": [],
  "experience": ""
}}

Resume:
{resume}
""")