"""
Candidate Extraction Service.

This service is responsible for extracting structured candidate
information from a resume PDF using the ResumeParser and Gemini LLM.
"""

import json
from pathlib import Path

from pydantic import ValidationError

from app.llm.gemini_client import GeminiClient
from app.models.candidates import Candidate
from app.prompts.extraction_prompts import (
    SYSTEM_PROMPT,
    build_extraction_prompt,
)
from app.tools.resume_parser import ResumeParser
from app.utils.logger import setup_logger


class CandidateExtractionService:
    """
    Service responsible for converting a resume PDF
    into a validated Candidate object.
    """

    def __init__(self):
        self.logger = setup_logger(self.__class__.__name__)

        self.resume_parser = ResumeParser()
        self.llm = GeminiClient()

    def extract(self, resume_path: str | Path) -> Candidate:
        """
        Extract candidate information from a resume.

        Parameters
        ----------
        resume_path : str | Path
            Path to the candidate resume PDF.

        Returns
        -------
        Candidate
            Validated Candidate model.
        """

        self.logger.info("Starting candidate extraction...")

        # Step 1
        resume_text = self.resume_parser.extract_text(resume_path)

        # Step 2
        user_prompt = build_extraction_prompt(resume_text)

        # Step 3
        response = self.llm.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
        )

        # Step 4
        try:
            candidate_dict = json.loads(response)

        except json.JSONDecodeError as e:
            self.logger.error("Failed to parse Gemini response.")

            raise ValueError(
                "Gemini returned an invalid JSON response."
            ) from e

        # Step 5
        try:
            candidate = Candidate.model_validate(candidate_dict)

        except ValidationError as e:
            self.logger.error("Candidate validation failed.")

            raise ValueError(
                "Extracted candidate data is invalid."
            ) from e

        self.logger.info("Candidate extracted successfully.")

        return candidate