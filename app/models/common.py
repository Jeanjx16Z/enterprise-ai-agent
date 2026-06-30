from typing import Optional

from pydantic import BaseModel, Field


class Experience(BaseModel):
    """
    Represents a candidate's professional work experience.
    """

    company: str = Field(..., description="Company name")
    position: str = Field(..., description="Job title")
    duration: Optional[str] = Field(
        default=None,
        description="Employment duration (e.g., 'Jan 2023 - Present')",
    )
    description: Optional[str] = Field(
        default=None,
        description="Summary of responsibilities and achievements",
    )


class Education(BaseModel):
    """
    Represents a candidate's educational background.
    """

    institution: str = Field(..., description="University or school name")
    degree: Optional[str] = Field(
        default=None,
        description="Degree obtained (e.g., Bachelor's, Master's)",
    )
    major: Optional[str] = Field(
        default=None,
        description="Field of study",
    )
    graduation_year: Optional[int] = Field(
        default=None,
        description="Graduation year",
    )


class Certification(BaseModel):
    """
    Represents a professional certification.
    """

    name: str = Field(..., description="Certification name")
    issuer: Optional[str] = Field(
        default=None,
        description="Certification provider",
    )
    issue_date: Optional[str] = Field(
        default=None,
        description="Certification issue date",
    )
    expiration_date: Optional[str] = Field(
        default=None,
        description="Certification expiration date",
    )


class Project(BaseModel):
    """
    Represents a personal, academic, or professional project.
    """

    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(
        default=None,
        description="Project summary",
    )
    technologies: list[str] = Field(
        default_factory=list,
        description="Technologies used in the project",
    )
    github_url: Optional[str] = Field(
        default=None,
        description="GitHub repository URL",
    )