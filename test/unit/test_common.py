from app.models.common import Experience

experience = Experience(
    company="ABC Technology",
    position="AI Engineer",
    duration="2024 - Present",
)

print(experience.model_dump())