def resume_analysis_prompt(resume_text: str) -> str:
    return f"""
You are an experienced Senior HR Manager, ATS (Applicant Tracking System) Expert,
Technical Recruiter, Career Coach, and Software Engineering Hiring Manager.

Your task is to analyze the following resume professionally.

Return your response using ONLY Markdown.

# Resume

{resume_text}

---

# Instructions

Analyze the resume carefully.

Provide the following sections:

# 📊 ATS Score

Give an ATS Compatibility Score out of 100.

Explain why.

---

# 📝 Professional Summary

Write a short summary about the candidate.

---

# 💪 Strengths

List the strongest points.

---

# ⚠ Weaknesses

Mention weaknesses that may reduce interview chances.

---

# ❌ Missing Skills

List missing technical skills.

---

# 🚀 Recommended Projects

Suggest 5 impressive projects based on the resume.

---

# 📚 Recommended Certifications

Recommend certifications that improve employability.

---

# 🎯 Career Recommendations

Suggest suitable job roles.

---

# 🎤 Interview Preparation

Mention important interview topics.

---

# 📈 Resume Improvement Suggestions

Give practical suggestions to improve the resume.

---

# ⭐ Final Verdict

Provide an overall evaluation.

Keep the response professional, structured, and easy to read.

Do not generate fake information.

If information is missing, clearly mention it.
"""