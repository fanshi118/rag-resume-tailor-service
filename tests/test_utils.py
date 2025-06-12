import pytest
from file_utils import load_text
from docx import Document
import tempfile

def test_load_text_txt():
    with tempfile.NamedTemporaryFile(mode='w+', suffix=".txt", delete=False) as f:
        f.write("Sample resume text.")
        f.seek(0)
        content, ext = load_text(f)
        assert "Sample resume" in content
        assert ext == "txt"

def test_load_text_docx():
    doc = Document()
    doc.add_paragraph("Sample docx resume.")
    path = tempfile.NamedTemporaryFile(delete=False, suffix=".docx").name
    doc.save(path)
    with open(path, "rb") as f:
        content, ext = load_text(f)
        assert "Sample docx" in content
        assert ext == "docx"
