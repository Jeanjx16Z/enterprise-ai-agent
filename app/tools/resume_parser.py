from pathlib import Path

import fitz

from app.utils.logger import setup_logger


class ResumeParser:
    """
    Extracts raw text from PDF resumes.

    Responsibilities:
    - Open PDF files
    - Extract text from all pages
    - Return raw text

    This class does NOT perform:
    - Information extraction
    - Skill matching
    - AI reasoning
    """

    def __init__(self):
        self.logger = setup_logger(self.__class__.__name__)

    def extract_text(self, pdf_path: str) -> str:
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"Resume not found: {pdf_path}")

        self.logger.info(f"Reading resume: {pdf_path.name}")

        document = fitz.open(pdf_path)

        try:
            self.logger.info(f"Total pages: {document.page_count}")

            text = "\n".join(
                page.get_text()
                for page in document
            )

            self.logger.info("Resume text extracted successfully.")

            return text.strip()

        finally:
            document.close()