import json


def resume_analysis_prompt(resume_text: str):

    schema = {
        "ats_score": 0,
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
You are an ATS System, HR Manager and Career Coach.

Analyze the following resume.

Return ONLY valid JSON.

JSON format:

{json.dumps(schema, indent=2)}

Resume:

{resume_text}

Do NOT return markdown.

Do NOT explain anything.

Only JSON.
"""