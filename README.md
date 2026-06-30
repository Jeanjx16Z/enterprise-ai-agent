# Enterprise AI Agent

> AI-powered recruitment system that automates candidate extraction from resumes using Google Gemini as the LLM backbone.

---

## Overview

Enterprise AI Agent is a modular Python application designed to streamline the recruitment process. It parses PDF resumes, extracts structured candidate information using a large language model (Google Gemini), and validates the output against strict Pydantic data models.

The architecture is intentionally decoupled — business logic is independent of any specific LLM provider, making it straightforward to swap out Gemini for OpenAI, Claude, or any other model in the future.

---

## Features

- **PDF Resume Parsing** — Extracts raw text from candidate resumes using PyMuPDF
- **LLM-Powered Extraction** — Uses Google Gemini to extract structured candidate data from unstructured resume text
- **Structured Data Models** — Validates all extracted data with Pydantic models (Candidate, JobDescription, Experience, Education, Certification, Project)
- **Provider-Agnostic LLM Interface** — `BaseLLM` abstract class makes it easy to plug in any LLM provider
- **Centralized Logging** — Consistent, timestamped logging across all modules
- **Environment-Based Configuration** — API keys and model settings managed via `.env`

---

## Project Structure

```
enterprise-ai-agent/
│
├── app/
│   ├── llm/
│   │   ├── base_llm.py                  # Abstract base class for all LLM providers
│   │   └── gemini_client.py             # Google Gemini implementation
│   │
│   ├── models/
│   │   ├── candidates.py                # Candidate domain model
│   │   ├── job_descriptions.py          # JobDescription domain model
│   │   └── common.py                    # Shared models (Experience, Education, Certification, Project)
│   │
│   ├── prompts/
│   │   └── extraction_prompts.py        # System & user prompt templates for extraction
│   │
│   ├── services/
│   │   └── candidate_extraction_service.py  # Orchestrates PDF parsing + LLM extraction
│   │
│   ├── tools/
│   │   └── resume_parser.py             # PDF text extraction using PyMuPDF
│   │
│   └── utils/
│       ├── config.py                    # Project-wide configuration & env vars
│       └── logger.py                    # Logger factory
│
├── agents/                              # (Upcoming) Autonomous agent definitions
│
├── data/
│   ├── candidates/                      # Input PDF resumes
│   ├── expected_result/                 # Expected extraction outputs (for testing)
│   └── job_descriptions/                # Job description files
│
├── test/
│   └── unit/
│       ├── test_candidates.py           # Candidate model test
│       ├── test_common.py               # Common model test
│       ├── test_config.py               # Config loading test
│       ├── test_gemini_client.py        # Gemini API integration test
│       ├── test_job_descriptions.py     # JobDescription model test
│       ├── test_logger.py               # Logger test
│       └── test_resume_parser.py        # PDF parsing test
│
├── utils/                               # (Upcoming) Shared utility scripts
├── .env                                 # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Architecture

The extraction pipeline follows a clean, linear flow:

```
PDF Resume
    │
    ▼
ResumeParser          (PyMuPDF — extracts raw text)
    │
    ▼
build_extraction_prompt   (injects resume text into prompt template)
    │
    ▼
GeminiClient.generate()   (calls Gemini API with system + user prompt)
    │
    ▼
JSON Response
    │
    ▼
Candidate.model_validate()  (Pydantic validation)
    │
    ▼
Candidate Object
```

The `CandidateExtractionService` orchestrates all steps above as a single `extract(resume_path)` call.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| LLM | Google Gemini 2.5 Flash (`google-genai`) |
| PDF Parsing | PyMuPDF (`fitz`) |
| Data Validation | Pydantic v2 |
| Configuration | python-dotenv |
| Web Framework | Streamlit / Uvicorn (prepared) |
| Logging | Python standard `logging` |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/enterprise-ai-agent.git
cd enterprise-ai-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

You can get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## Usage

### Run candidate extraction

```python
from app.services.candidate_extraction_service import CandidateExtractionService

service = CandidateExtractionService()
candidate = service.extract("data/candidates/your_resume.pdf")

print(candidate.name)
print(candidate.technical_skills)
print(candidate.model_dump())
```

---

## Running Tests

All test files are located in `test/unit/`. Run them individually from the project root:

```bash
# Test PDF parsing
python test/unit/test_resume_parser.py

# Test Gemini API connection
python test/unit/test_gemini_client.py

# Test Candidate model
python test/unit/test_candidates.py

# Test JobDescription model
python test/unit/test_job_descriptions.py

# Test configuration loading
python test/unit/test_config.py

# Test logger
python test/unit/test_logger.py
```

> Make sure your `.env` file is set up correctly before running tests that call the Gemini API.

---

## Data Models

### `Candidate`
| Field | Type | Description |
|---|---|---|
| `name` | `str` | Full name |
| `email` | `EmailStr` | Email address |
| `phone` | `str` | Phone number |
| `location` | `str` | Current location |
| `technical_skills` | `list[str]` | Technical skills |
| `soft_skills` | `list[str]` | Soft skills |
| `experiences` | `list[Experience]` | Work history |
| `education` | `list[Education]` | Academic background |
| `certifications` | `list[Certification]` | Professional certifications |
| `projects` | `list[Project]` | Portfolio projects |
| `languages` | `list[str]` | Spoken languages |
| `resume_text` | `str` | Raw extracted resume text |

### `JobDescription`
| Field | Type | Description |
|---|---|---|
| `title` | `str` | Job title |
| `department` | `str` | Business unit |
| `required_skills` | `list[str]` | Mandatory skills |
| `preferred_skills` | `list[str]` | Nice-to-have skills |
| `minimum_experience_years` | `int` | Minimum experience required |
| `education_requirement` | `str` | Education level required |
| `responsibilities` | `list[str]` | Job responsibilities |
| `qualifications` | `list[str]` | Additional qualifications |

---

## Extending with a New LLM Provider

To add a new LLM (e.g., OpenAI), create a new class that extends `BaseLLM`:

```python
from app.llm.base_llm import BaseLLM

class OpenAIClient(BaseLLM):

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        # your implementation here
        ...

    def health_check(self) -> bool:
        # your implementation here
        ...
```

Then swap it into `CandidateExtractionService` without touching any other part of the system.

---

## Roadmap

- [ ] Job Description extraction from PDF/text
- [ ] Skill matching engine (Candidate vs JobDescription)
- [ ] Scoring engine with weighted criteria
- [ ] AI-powered candidate recommendation
- [ ] Streamlit dashboard for recruiter UI
- [ ] Integration tests with expected result validation
- [ ] Autonomous agent orchestration (`agents/` module)

---

## License

This project is for personal and educational use. No license is currently applied.

---

## Author

**Jean Jeasen**  
AI Engineer
