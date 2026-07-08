import streamlit as st  # type: ignore[import]

from utils.pdf_reader import extract_text_from_pdf
from utils.prompts import resume_analysis_prompt
from utils.gemini import analyze_resume

try:
    from fpdf import FPDF
except ImportError:
    FPDF = None


def create_pdf_report(result: dict) -> bytes:
    if FPDF is None:
        raise ImportError(
            "FPDF library is required to generate PDF reports. "
            "Install it with `pip install fpdf`."
        )

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "AI Resume Analysis Report", ln=True, align="C")
    pdf.ln(5)

    def write_section(title: str, content):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("Arial", "", 11)

        if isinstance(content, list):
            for item in content:
                pdf.multi_cell(0, 8, f"- {item}")
        else:
            pdf.multi_cell(0, 8, content or "N/A")

        pdf.ln(3)

    write_section("Summary", result.get("summary", "N/A"))
    write_section("Strengths", result.get("strengths", []))
    write_section("Weaknesses", result.get("weaknesses", []))
    write_section("Missing Skills", result.get("missing_skills", []))
    write_section("Recommended Projects", result.get("recommended_projects", []))
    write_section("Recommended Certifications", result.get("recommended_certifications", []))
    write_section("Career Roles", result.get("career_roles", []))
    write_section("Interview Topics", result.get("interview_topics", []))
    write_section("Improvements", result.get("improvements", []))
    write_section("Final Verdict", result.get("final_verdict", "N/A"))

    return pdf.output(dest="S").encode("latin-1")

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

st.subheader("💼 Job Description (Optional)")

job_description = st.text_area(
    "Paste the Job Description here",
    height=200,
    placeholder="Paste the company's job description..."
)

if uploaded_file:

    st.success("Resume Uploaded Successfully ✅")
    st.write(uploaded_file.name)

    if st.button("🚀 Analyze Resume", use_container_width=True):

        try:

            with st.spinner("📖 Reading Resume..."):
                resume = extract_text_from_pdf(uploaded_file)

            with st.spinner("🤖 Analyzing with Gemini AI..."):
                prompt = resume_analysis_prompt(
                    resume,
                    job_description
                )

                result = analyze_resume(prompt)

            st.success("Analysis Completed Successfully 🎉")

            st.divider()

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("ATS Score", f"{result['ats_score']}/100")

            with col2:
                st.metric("JD Match", f"{result['jd_match_score']}/100")

            with col3:
                st.metric("Resume", "Analyzed")

            with col4:
                st.metric("AI", "Gemini")

            st.divider()

            st.subheader("📝 Summary")
            st.write(result["summary"])

            st.subheader("💪 Strengths")
            for item in result["strengths"]:
                st.success(item)

            st.subheader("⚠ Weaknesses")
            for item in result["weaknesses"]:
                st.warning(item)

            st.subheader("❌ Missing Skills")
            for item in result["missing_skills"]:
                st.error(item)

            st.subheader("🚀 Recommended Projects")
            for item in result["recommended_projects"]:
                st.info(item)

            st.subheader("📚 Recommended Certifications")
            for item in result["recommended_certifications"]:
                st.write("✅", item)

            st.subheader("🎯 Career Roles")
            for item in result["career_roles"]:
                st.write("💼", item)

            st.subheader("🎤 Interview Topics")
            for item in result["interview_topics"]:
                st.write("📌", item)

            st.subheader("📈 Improvements")
            for item in result["improvements"]:
                st.write("➡", item)

            st.subheader("⭐ Final Verdict")
            st.success(result["final_verdict"])

            st.divider()

            if st.button("📄 Generate PDF Report"):

                pdf_file = create_pdf_report(result)

                with open(pdf_file, "rb") as file:

                    st.download_button(
                        label="⬇ Download Report",
                        data=file,
                        file_name="AI_Resume_Analysis_Report.pdf",
                        mime="application/pdf"
                    )

        except Exception as e:
            st.error(f"Error: {e}")