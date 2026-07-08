import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

st.markdown(
    """
Upload your resume and get AI-powered insights using **Google Gemini**.

### You'll receive:
- ✅ ATS Score
- ✅ Resume Summary
- ✅ Strengths
- ✅ Weaknesses
- ✅ Missing Skills
- ✅ Improvement Suggestions
"""
)

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")

    st.info(f"Filename: {uploaded_file.name}")

    st.button("🚀 Analyze Resume")