from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from app.models.common import (
    Certification,
    Education,
    Experience,
    Project,
)


class Candidate(BaseModel):
    """
    Represents a job candidate within the recruitment system.

    This model serves as the central domain object shared across
    Resume Parser, Skill Matcher, Scoring Engine, LLM Service,
    and Report Generator.
    """

    # ==========================
    # Personal Information
    # ==========================

    name: str = Field(..., description="Candidate full name")

    email: Optional[EmailStr] = Field(
        default=None,
        description="Candidate email address",
    )

    phone: Optional[str] = Field(
        default=None,
        description="Candidate phone number",
    )

    location: Optional[str] = Field(
        default=None,
        description="Candidate location",
    )

    # ==========================
    # Skills
    # ==========================

    technical_skills: list[str] = Field(
        default_factory=list,
        description="Technical skills",
    )

    soft_skills: list[str] = Field(
        default_factory=list,
        description="Soft skills",
    )

    # ==========================
    # Professional Experience
    # ==========================

    experiences: list[Experience] = Field(
        default_factory=list,
        description="Professional work experiences",
    )

    # ==========================
    # Education
    # ==========================

    education: list[Education] = Field(
        default_factory=list,
        description="Educational background",
    )

    # ==========================
    # Certifications
    # ==========================

    certifications: list[Certification] = Field(
        default_factory=list,
        description="Professional certifications",
    )

    # ==========================
    # Projects
    # ==========================

    projects: list[Project] = Field(
        default_factory=list,
        description="Projects completed by the candidate",
    )

    # ==========================
    # Languages
    # ==========================

    languages: list[str] = Field(
        default_factory=list,
        description="Languages spoken by the candidate",
    )

    # ==========================
    # Resume Metadata
    # ==========================

    resume_text: Optional[str] = Field(
        default=None,
        description="Raw text extracted from the uploaded resume",
    )