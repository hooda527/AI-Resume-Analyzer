import json

def resume_analysis_prompt(resume_text: str, job_description: str = ""):

    schema = {
        "ats_score": 0,
        "jd_match_score": 0,
        "summary": "",
        "strengths": [],
        "weaknesses": [],
        "missing_skills": [],
        "recommended_projects": [],
        "recommended_certifications": [],
        "career_roles": [],
        "interview_topics": [],
        "improvements": [],
        "final_verdict": ""
    }

    return f"""
You are an experienced HR Manager, ATS Expert, Technical Recruiter and Career Coach.

Analyze this resume professionally.

Resume:

{resume_text}

Job Description:

{job_description}

Return ONLY valid JSON.

JSON Schema:

{json.dumps(schema, indent=2)}

Rules:

- ATS Score must be between 0 and 100.
- JD Match Score must be between 0 and 100.
- Recommend missing skills based on the Job Description.
- Keep answers short and professional.
- Return ONLY JSON.
"""