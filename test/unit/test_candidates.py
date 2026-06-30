from app.models.candidates import Candidate
from app.models.common import Experience

candidate = Candidate(
    name="Jean Jeasen",
    email="jean@example.com",
    technical_skills=["Python", "SQL", "Machine Learning"],
    experiences=[
        Experience(
            company="ABC Technology",
            position="AI Engineer",
            duration="2024 - Present",
        )
    ],
)

print(candidate.model_dump())