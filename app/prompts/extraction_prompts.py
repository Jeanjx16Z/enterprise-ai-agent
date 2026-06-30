"""
Prompt templates for candidate information extraction.

This module contains the system instruction and user prompt
used by the Recruitment Agent to extract structured candidate
information from a resume.

The prompt is intentionally separated from the Gemini service
to improve maintainability and allow prompt iteration without
changing application logic.
"""

SYSTEM_PROMPT = """
You are an expert AI Recruitment Assistant.

Your responsibility is to extract structured candidate information
from a resume.

Rules:

1. Extract only information explicitly stated in the resume.
2. Do not guess or hallucinate missing information.
3. If a field is missing, return null or an empty list.
4. Preserve the original wording whenever possible.
5. Return valid JSON only.
6. Do not include explanations, markdown, or additional text.
"""


USER_PROMPT_TEMPLATE = """
Extract the following information from the resume.

Required Fields:

- name
- email
- phone
- location
- technical_skills
- soft_skills
- experiences
- education
- certifications
- projects
- languages

Resume:

--------------------
{resume_text}
--------------------

Return JSON with the following structure:

{
    "name": "",
    "email": "",
    "phone": "",
    "location": "",
    "technical_skills": [],
    "soft_skills": [],
    "experiences": [],
    "education": [],
    "certifications": [],
    "projects": [],
    "languages": []
}
"""

def build_extraction_prompt(resume_text: str) -> str:
    """
    Build the user prompt by injecting the resume text.

    Parameters
    ----------
    resume_text : str
        Extracted text from the candidate's resume.

    Returns
    -------
    str
        Formatted prompt ready to be sent to the LLM.
    """

    return USER_PROMPT_TEMPLATE.format(
        resume_text=resume_text
    )