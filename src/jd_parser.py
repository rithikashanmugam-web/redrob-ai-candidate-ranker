from docx import Document


def load_job_description(filepath):

    doc = Document(filepath)

    full_text = []

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()

        if text:
            full_text.append(text)

    return "\n".join(full_text)