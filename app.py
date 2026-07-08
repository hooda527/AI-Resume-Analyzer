import streamlit as st
from utils.pdf_reader import extract_text_from_pdf

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

st.markdown("""
Upload your resume and receive AI-powered feedback.

### Features

- ✅ ATS Score
- ✅ Resume Summary
- ✅ Strengths
- ✅ Weaknesses
- ✅ Missing Skills
- ✅ Improvement Suggestions
""")

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    st.write("### Resume Information")

    st.write(f"**Filename:** {uploaded_file.name}")

    if st.button("Extract Resume Text"):

        with st.spinner("Reading PDF..."):

            resume_text = extract_text_from_pdf(uploaded_file)

        st.success("Text extracted successfully!")

        st.subheader("Resume Preview")

        st.text_area(
            "Extracted Text",
            resume_text,
            height=350
        )