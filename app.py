import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.prompts import resume_analysis_prompt
from utils.gemini import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.block-container{
    padding-top:2rem;
}

.card{
    background:#1E1E1E;
    padding:20px;
    border-radius:15px;
    border:1px solid #333333;
    box-shadow:0px 0px 15px rgba(0,0,0,.3);
}

.metric{
    text-align:center;
    padding:15px;
    border-radius:10px;
    background:#262730;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ---------------- #

st.title("🤖 AI Resume Analyzer")

st.caption("Powered by Google Gemini AI")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Model", "Gemini")

with col2:
    st.metric("Resume Format", "PDF")

with col3:
    st.metric("Status", "Ready")

st.divider()

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume Uploaded Successfully ✅")

    st.write(uploaded_file.name)

    if st.button("🚀 Analyze Resume", use_container_width=True):

        try:

            with st.spinner("Reading Resume..."):

                resume = extract_text_from_pdf(uploaded_file)

            with st.spinner("Analyzing with Gemini AI..."):

                prompt = resume_analysis_prompt(resume)

                result = analyze_resume(prompt)

            st.success("Analysis Completed Successfully 🎉")

            st.divider()

            st.markdown(result)

        except Exception as e:

            st.error(e)