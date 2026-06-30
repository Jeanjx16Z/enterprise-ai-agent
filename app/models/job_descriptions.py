from typing import Optional

from pydantic import BaseModel, Field


class JobDescription(BaseModel):
    """
    Represents a job description used for candidate evaluation.

    This model acts as the source of truth for recruitment
    requirements and is consumed by the Skill Matcher,
    Scoring Engine, and AI Recommendation modules.
    """

    # ==========================
    # Basic Information
    # ==========================

    title: str = Field(
        ...,
        description="Job title",
    )

    department: Optional[str] = Field(
        default=None,
        description="Department or business unit",
    )

    # ==========================
    # Skills
    # ==========================

    required_skills: list[str] = Field(
        default_factory=list,
        description="Mandatory technical skills",
    )

    preferred_skills: list[str] = Field(
        default_factory=list,
        description="Preferred technical skills",
    )

    # ==========================
    # Experience
    # ==========================

    minimum_experience_years: Optional[int] = Field(
        default=None,
        description="Minimum years of professional experience",
    )

    # ==========================
    # Education
    # ==========================

    education_requirement: Optional[str] = Field(
        default=None,
        description="Minimum education requirement",
    )

    # ==========================
    # Responsibilities
    # ==========================

    responsibilities: list[str] = Field(
        default_factory=list,
        description="Main job responsibilities",
    )

    qualifications: list[str] = Field(
        default_factory=list,
        description="Additional qualifications",
    )

    # ==========================
    # Original Text
    # ==========================

    raw_text: Optional[str] = Field(
        default=None,
        description="Original job description text",
    )