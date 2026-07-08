from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


def create_pdf_report(result):

    file_path = "AI_Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(
        Paragraph(
            "AI Resume Analyzer Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))


    # Basic Sections
    sections = {
        "ATS Score": result.get("ats_score", "N/A"),
        "JD Match Score": result.get("jd_match_score", "N/A"),
        "Summary": result.get("summary", "N/A"),
        "Final Verdict": result.get("final_verdict", "N/A")
    }


    for title, value in sections.items():

        content.append(
            Paragraph(
                f"<b>{title}</b>",
                styles["Heading3"]
            )
        )

        content.append(
            Paragraph(
                str(value),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 12)
        )


    # List Sections
    list_sections = [
        ("Strengths", "strengths"),
        ("Weaknesses", "weaknesses"),
        ("Missing Skills", "missing_skills"),
        ("Recommended Projects", "recommended_projects"),
        ("Recommended Certifications", "recommended_certifications"),
        ("Career Roles", "career_roles"),
        ("Interview Topics", "interview_topics"),
        ("Improvements", "improvements")
    ]


    for title, key in list_sections:

        content.append(
            Paragraph(
                f"<b>{title}</b>",
                styles["Heading3"]
            )
        )


        items = result.get(key, [])

        if isinstance(items, list):

            for item in items:

                content.append(
                    Paragraph(
                        "• " + str(item),
                        styles["BodyText"]
                    )
                )

        else:

            content.append(
                Paragraph(
                    str(items),
                    styles["BodyText"]
                )
            )


        content.append(
            Spacer(1, 12)
        )


    doc.build(content)

    return file_path