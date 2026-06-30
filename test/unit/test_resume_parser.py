from pathlib import Path

from app.tools.resume_parser import ResumeParser


def contains_any_keyword(text: str, keywords: list[str]) -> bool:
    """
    Check whether any keyword exists in the extracted resume text.
    """
    text = text.upper()
    return any(keyword in text for keyword in keywords)


def main():
    parser = ResumeParser()

    resume_path = Path(
        "data/candidates/Jean_Jeasen_AI_Engineer.pdf"
    )

    text = parser.extract_text(resume_path)

    # Basic validation
    assert isinstance(text, str), "Output must be a string."
    assert len(text.strip()) > 0, "Resume text is empty."

    print("=" * 60)
    print("Resume Preview")
    print("=" * 60)
    print(text[:1000])
    print("=" * 60)

    print("Section Validation")
    print("=" * 60)

    print(
        "Contains Education Section :",
        contains_any_keyword(
            text,
            [
                "EDUCATION",
                "ACADEMIC",
                "ACADEMIC BACKGROUND",
            ],
        ),
    )

    print(
        "Contains Project Section :",
        contains_any_keyword(
            text,
            [
                "PROJECT",
                "PROJECTS",
                "PERSONAL PROJECT",
            ],
        ),
    )

    print(
        "Contains Certificate Section :",
        contains_any_keyword(
            text,
            [
                "CERTIFICATION",
                "CERTIFICATIONS",
                "CERTIFICATE",
                "CERTIFICATES",
                "LICENSE",
                "LICENSES",
            ],
        ),
    )

    print("=" * 60)

    print(f"Total Characters : {len(text)}")
    print(f"Total Words      : {len(text.split())}")

    print("=" * 60)


if __name__ == "__main__":
    main()