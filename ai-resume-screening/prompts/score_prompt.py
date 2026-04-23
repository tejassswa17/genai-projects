from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate.from_template("""
You are an AI recruiter.

Based on the matching result, assign a score from 0 to 100.

Rules:
- More matched skills → higher score
- More missing skills → lower score
- Do NOT assume anything
- ALWAYS provide a clear reason for the score
- Do NOT leave reason empty
- Return ONLY valid JSON (no extra text)

{{
  "score": 0,
  "reason": "explain briefly why this score was given"
}}

Matching Data:
{match_data}
""")