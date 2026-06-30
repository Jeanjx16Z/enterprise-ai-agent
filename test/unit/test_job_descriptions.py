from app.models.job_descriptions import JobDescription

jd = JobDescription(
    title="AI Engineer",
    department="Technology",
    required_skills=[
        "Python",
        "Machine Learning",
        "SQL",
    ],
    preferred_skills=[
        "Docker",
        "AWS",
    ],
    minimum_experience_years=2,
    education_requirement="Bachelor's Degree",
)

print(jd.model_dump())