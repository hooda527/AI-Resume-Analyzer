from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from uploaded PDF file.
    """

    try:
        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if not text.strip():
            return "No readable text found in this PDF."

        return text.strip()


    except Exception as e:
        raise Exception(
            f"Unable to read PDF file: {str(e)}"
        )