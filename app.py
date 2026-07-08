import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.prompts import resume_analysis_prompt
from utils.gemini import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

st.markdown("""
Analyze your resume using **Google Gemini AI**.

### Features

- 📊 ATS Score
- 💪 Strengths
- ⚠ Weaknesses
- ❌ Missing Skills
- 🚀 Recommended Projects
- 📚 Certifications
- 🎯 Career Suggestions
- 📝 Resume Improvement Tips
""")

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    st.write(f"**File:** {uploaded_file.name}")

    if st.button("🚀 Analyze Resume"):

        try:

            with st.spinner("📖 Reading Resume..."):

                resume_text = extract_text_from_pdf(uploaded_file)

            with st.spinner("🤖 Gemini AI is analyzing your resume..."):

                prompt = resume_analysis_prompt(resume_text)

                result = analyze_resume(prompt)

            st.success("Analysis Completed Successfully!")

            st.markdown("---")

            st.markdown(result)

        except Exception as e:

            st.error(f"Error: {e}")