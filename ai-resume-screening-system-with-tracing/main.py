from dotenv import load_dotenv
import os
import json

# 🔥 Load .env
load_dotenv()

# 🔍 Check if env loaded
print("Tracing:", os.getenv("LANGCHAIN_TRACING_V2"))
print("Project:", os.getenv("LANGCHAIN_PROJECT"))

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain

# 📂 Resume files
resumes = [
    "data/resume_strong.txt",
    "data/resume_avg.txt",
    "data/resume_weak.txt"
]

# 📂 Job description
with open("data/job.txt", "r") as f:
    job = f.read()

# 🔁 Process all resumes
for file in resumes:
    print(f"\n===== Processing {file} =====")

    with open(file, "r") as f:
        resume = f.read()

    # Step 1: Extract
    extracted = extract_chain.invoke({"resume": resume})
    resume_data = extracted.content

    # Step 2: Match
    matched = match_chain.invoke({
        "resume_data": resume_data,
        "job_description": job
    })
    match_data = matched.content
    match_json = json.loads(match_data)

    # Step 3: Score
    score_result = score_chain.invoke({
        "match_data": match_data
    })
    score_json = json.loads(score_result.content)

    # Final output
    final_output = {
        "score": score_json["score"],
        "matched_skills": match_json["matched_skills"],
        "missing_skills": match_json["missing_skills"],
        "explanation": score_json["reason"]
    }

    print(json.dumps(final_output, indent=2))